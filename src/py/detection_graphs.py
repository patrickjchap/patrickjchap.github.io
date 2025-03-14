import json
import os
import sys
from datetime import datetime
from itertools import cycle
import numpy as np

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as io

DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
palette = cycle(px.colors.qualitative.Plotly)
#palette = cycle(px.colors.sequential.PuBu)

COMPARISON_METHOD = {"Diff", "Trace"}

def generate_detection_rate_timeline(csv_filepath: str, output_path: str, comparison_method="Diff"):
    assert comparison_method in COMPARISON_METHOD
    print(comparison_method)

    df = pd.read_csv(csv_filepath)
    df = df.sort_values(by="Commit Fix Date")

    # Create figure
    fig = go.Figure()

    methods_to_plot = set(list(df["Methodology"]))
    for method in methods_to_plot:
        selected_df = df[df["Methodology"] == method]
        fig.add_trace(
            go.Scatter(
                name=method,
                x=list(selected_df["Commit Fix Date"]),
                y=list(selected_df[f"Reports in {comparison_method}"]),
                customdata=np.stack(
                    (
                        selected_df["Artifact Image Tag"],
                        selected_df["Times Ran"],
                        selected_df["URL"],
                    ),
                    axis=1
                ),
                hovertemplate="<br>".join([
                    "Commit Fix Date: %{x}",
                    "Detection Rate: %{y}",
                    "Artifact Image Tag: %{customdata[0]}",
                    "Times Ran: %{customdata[1]}",
                    "DIFF: <a href='%{customdata[2]}'>%{customdata[2]}</a>",
                ]),
                marker_color=next(palette)))

    # Set title
    fig.update_layout(
        title_text="Time series with buggy code artifacts and detection rates.",
        height=450,
        minreducedwidth=900,
    )
#   fig.update_traces(
#       hovertemplate="<br>".join([
#           "Commit Fix Date: %{x}",
#           "Detection Rate: %{y}",
#           "Artifact Image Tag: %{customdata[0]}",
#           "Times Ran: %{customdata[1]}",
#           "URL: %{customdata[2]}",
#       ])
#   )

    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )

    fig.write_html(output_path)

#def generate_pass_k_plot(csv_filepath: str, output_path: str):
#
#def generate_repair_summary_plot(csv_filepath: str, output_path: str):
#

if __name__ == "__main__":
    csv_path = os.path.join(
        os.path.dirname(__file__), "../../assets/csv/test_example.csv")
    rel_output_path = "../../assets/html/test_diff_timeline.html"
    output_path = os.path.join(
        os.path.dirname(__file__), rel_output_path) 
    comparison_method = "Diff"
    if len(sys.argv) > 1:
        output_path = os.path.abspath(sys.argv[1])
        if "diff" not in output_path:
            comparison_method = "Trace"
    generate_detection_rate_timeline(csv_path, output_path, comparison_method)
