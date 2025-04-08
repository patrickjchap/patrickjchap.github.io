import csv
import json


def csv_to_markdown_table(csv_filepath: str) -> str:
    table = ""
    with open(csv_filepath, "r") as csv_f:
        reader = csv.reader(csv_f)
        header = next(reader)

    table += "| " + " | ".join(header) + " |\n"
    table += "| " + " | ".join(["---"] * len(header)) + " |\n"

    for row in reader:
        table += "| " + " | ".join(row) + " |\n"

    return table

def json_to_html_table(json_filepath: str) -> str:
    with open(json_filepath) as f:
        artifact_runs = json.load(f)

    table_rows = ""
    for artifact_image_tag, runs in artifact_runs.items():
        for llm_methodology, run_info in runs.items():

     

    return f"""
    <table>                                                                         
     <thead>                                                                        
        <tr>                                                                        
            <th> Artifact Image Tag </th>                                           
            <th> LLM-based Analysis </th>                                           
            <th> Total Runs </th>                                                   
            <th> Reports Matching Diff </th>                                        
            <th> Reports Matching Trace </th>                                       
            <th> Diff URL </th>                                                     
        </tr>                                                                       
      </thead> 
      {table_rows}
    </table>
    """
