import json
from datetime import datetime

import plotly.express as px
import plotly.io as io

DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

def generate_detection_rate_timeline(json_filepath: str, output_path: str):
    with open(json_filepath) as f:
        detection_results = json.load(f)

    for artifact_id, evaluation_results in detection_results.items():
        for evaluation_method, results in evaluation_results.items():
        

    return True

#def generate_pass_k_plot(csv_filepath: str, output_path: str):
#
#def generate_repair_summary_plot(csv_filepath: str, output_path: str):
#

