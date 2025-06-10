""" Dumps the JSON results file to a CSV table for the site. """
import json
import glob
import os

from bugswarm.common.rest_api.database_api import DatabaseAPI

json_path = "./assets/json/"
GPT_NAME_TO_CUTOFF_DATE = {
    "gpt-4o-mini-2024-07-18": "2024-07-18",
    "gpt-4.1-mini-2025-04-14": "2025-04-14",
    "gpt-4.1-nano-2025-04-14": "2025-04-15"
}
BUGSWARM_TOKEN = "YOUR-API-KEY"

""" CSV FORMAT

Artifact Image Tag,LLM,Methodology,Total Runs,Detection Rate - Diff,Detection Rate - Trace,Knowledge Cutoff Date,Commit Fix Date,Bug Report,Diff URL

"""

def repo_created_at(full_name: str, token: str=None) -> str:
    try:
        owner, repo = full_name.split("/", 1)
    except ValueError:
        raise SystemExit("Repository must be in the form <owner>/<repo>")

    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Accept": "application/vnd.github+json"}
    if token:                      # authenticated calls enjoy a 5 000-request/hour limit
        headers.update({
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28"
        })

    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    return resp.json()["created_at"]   # e.g. "2017-01-09T02:41:41Z"

def populate_artifact_metadata(artifact_ids):
    artifact_metadata = dict()
    api_filter = '{"status": {"$in": ["active", "candidate"]}}'
    api = DatabaseAPI(token=BUGSWARM_TOKEN)
    artifacts = api.filter_artifacts(api_filter)
    for artifact in artifacts:
        artifact_id = artifact["image_tag"]
        artifact_metadata[artifact_id] = dict()
        if artifact_id not in artifact_ids:
            continue

        fix_commit_date = artifact["passed_job"]["committed_at"].split("T")[0]
        artifact_metadata[artifact_id]["fix_date"] = fix_commit_date
        passed_job_sha = artifact["passed_job"]["trigger_sha"]
        failed_job_sha = artifact["failed_job"]["trigger_sha"]
        repo = artifact["repo"]
        artifact_metadata[artifact_id]["diff_url"] = f"https://github.com/{repo}/compare/{failed_job_sha}...{passed_job_sha}"

    return artifact_metadata

def get_random_example_reports_artifacts(bug_reports):
    """ Gets the first valid bug report from the reports."""
    example_reports = dict()
    for run_num, artifact_id_to_reports in bug_reports.items():
        if "run" not in run_num:
            continue
        for artifact_id, file_reports in artifact_id_to_reports.items():
            if artifact_id in example_reports:
                continue
            for file_name, bug_reports in file_reports.items():
                for report in bug_reports:
                    file_base = os.path.basename(file_name)
                    string_report = f"File: {file_base} Line: {report['line']}"
                    example_reports[artifact_id] = string_report

    return example_reports

print("Artifact Image Tag,Diff URL,Commit Fix Date,Total Runs,LLM,LLM Knowledge Cutoff Date,Methodology,Detection Rate - Diff,Detection Rate - Trace,Bug Report Example")
artifact_metadata = None
for filename in glob.glob(os.path.join(json_path, "*.json")):
    with open(filename, encoding='utf-8') as f:
        gpt_name = None
        for name in GPT_NAME_TO_CUTOFF_DATE.keys():
            if name in filename:
                gpt_name = name
                break
        if not gpt_name:
            raise ValueError("File name does not have proper GPT name?")

        method_name = None
        if "NULL-CALL" in filename:
            method_name = "NCR"
        elif "Baseline-BUGS" in filename:
            method_name = "BaseBUGS"
        elif "Baseline-NPE" in filename:
            method_name = "BaseNPE"
        elif "Dataflow" in filename:
            method_name = "Dataflow"
        elif "CWE" in filename:
            method_name = "CWE"
        if not method_name:
            raise ValueError(f"File name: {filename} does not have proper method name?")

        if "-COT-" in filename:
            method_name += " + CoT"


        #Printing the CSV header.
        results = json.load(f)
        #for run_num, experiment_metrics in results.items():
        artifact_ids = list(results["experiment_metrics"]["whole_experiment_per_artifact_metrics"].keys())
        example_reports = None
        for artifact_id, per_artifact_metrics in results["experiment_metrics"]["whole_experiment_per_artifact_metrics"].items():
            if not example_reports:
                example_reports = get_random_example_reports_artifacts(results)
            if not artifact_metadata:
                artifact_metadata = populate_artifact_metadata(artifact_ids)

            total_runs = per_artifact_metrics["total_runs"]
            detection_rate_diff = per_artifact_metrics["detection_rate_diff"]
            detection_rate_trace = per_artifact_metrics["detection_rate_trace"]
            llm_cutoff_date = GPT_NAME_TO_CUTOFF_DATE[gpt_name]
            diff_url = artifact_metadata[artifact_id]["diff_url"]
            fix_date = artifact_metadata[artifact_id]["fix_date"]
            example_report = "None"
            if artifact_id in example_reports:
                example_report = example_reports[artifact_id]
            print(f"{artifact_id},{diff_url},{fix_date},{total_runs},{gpt_name},{llm_cutoff_date},{method_name},{detection_rate_diff},{detection_rate_trace},{example_report}")
