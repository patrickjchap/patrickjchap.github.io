import json
import os
import sys
from datetime import datetime
from itertools import cycle
import numpy as np

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as io

ARTIFACT_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
MODEL_DATE_FORMAT = "%Y-%m-%d"
palette = cycle(px.colors.qualitative.Plotly)
#palette = cycle(px.colors.sequential.PuBu)

COMPARISON_METHOD = {"Diff", "Trace"}

def __ceildiv(a, b):
    return -(a // -b)

def generate_detection_bar_plot(csv_filepath: str, output_path: str, comparison_method="Diff"):
    assert comparison_method in COMPARISON_METHOD
    print(comparison_method)
    num_steps = 21

    df = pd.read_csv(csv_filepath)
    df = df.sort_values(by="Commit Fix Date")
    df["LLM and Analysis Method"] = df.apply(lambda r: f"{r['LLM']} {r['Methodology']}", axis=1)
    unique_methods = df["LLM and Analysis Method"].unique()
    num_unique_methods = df["LLM and Analysis Method"].nunique()

    fig = go.Figure()
    fig = make_subplots(rows=df["LLM and Analysis Method"].nunique(), subplot_titles=unique_methods, vertical_spacing=0.20)
    max_y = 0
    
    for j, method in enumerate(df["LLM and Analysis Method"].unique()):
        selected_df = df[df["LLM and Analysis Method"] == method]
        for i in range(num_steps):
            threshold = float(i) / 20.0
            passing_before = len(selected_df[(selected_df[f"Bug Detection - {comparison_method}"] >= threshold) & (selected_df["LLM Knowledge Cutoff Date"] <= selected_df["Commit Fix Date"])])
            failing_before = len(selected_df[(selected_df[f"Bug Detection - {comparison_method}"] < threshold) & (selected_df["LLM Knowledge Cutoff Date"] <= selected_df["Commit Fix Date"])])
            passing_after = len(selected_df[(selected_df[f"Bug Detection - {comparison_method}"] >= threshold) & (selected_df["LLM Knowledge Cutoff Date"] > selected_df["Commit Fix Date"])])
            failing_after = len(selected_df[(selected_df[f"Bug Detection - {comparison_method}"] < threshold) & (selected_df["LLM Knowledge Cutoff Date"] > selected_df["Commit Fix Date"])])
            passing_total = len(selected_df[(selected_df[f"Bug Detection - {comparison_method}"] >= threshold)])
            failing_total = len(selected_df[(selected_df[f"Bug Detection - {comparison_method}"] < threshold)])

            max_y = max(passing_before, failing_before, passing_after, failing_after, passing_total, failing_total, max_y)

            fig.add_trace(
                go.Bar(
                    x=["Passing Before", "Failing Before", "Passing After", "Failing After", "Total Passing", "Total Failing"],
                    y=[passing_before, failing_before, passing_after, failing_after, passing_total, failing_total],
                    width=0.2,
                    marker_color=['blue', 'red', 'blue', 'red', 'cyan', 'orange'],
                    name=f"{method}",
                    visible=False,
                ),
                row=j+1,
                col=1,
            )

    fig.update_layout(
            title_text=f"Total number of artifacts with bug detected against {comparison_method} given detect@k threshold: 50.0%.",
            height=800,
    )
    fig.update_yaxes(title="Number of artifacts above detect@k threshold.", row=__ceildiv(num_unique_methods, 2), col=1)
    fig.update_yaxes(range=[0, max_y])
    fig.update_xaxes(title="Commit date before or after LLM knowledge cutoff.", row=num_unique_methods, col=1)

    for j in range(num_unique_methods):
        fig.data[10+((j) * num_steps)].visible = True

    steps = []
    for i in range(num_steps):
        step = dict(
            method="update",
            args=[
                    {"visible": [False] * len(fig.data)},
                    {"title": f"Total number of artifacts with bug detected against {comparison_method} given detect@k threshold: {i* 5.0}%."},
                 ],
        )

        for j in range(df["LLM and Analysis Method"].nunique()):
            step["args"][0]["visible"][i+((j) * num_steps)] = True
        steps.append(step)

    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Detect@k Threshold: 5.0 * "},
        pad={"t": 50},
        steps=steps,
    )]


    fig.update_layout(
        sliders=sliders
    )

    fig.write_html(output_path)

def generate_detection_rate_histogram(csv_filepath: str, output_path: str, comparison_method="Diff"):
    assert comparison_method in COMPARISON_METHOD
    print(comparison_method)

    df = pd.read_csv(csv_filepath)
    df = df.sort_values(by="Commit Fix Date")
    df["LLM and Analysis Method"] = df.apply(lambda r: f"{r['LLM']} + {r['Methodology']}", axis=1)

    # Create figure
    fig = px.histogram(
        df, 
        x=f"Bug Detection - {comparison_method}",
        color="LLM and Analysis Method",
        barmode="overlay",
    )
 
    # Set title
    fig.update_layout(
        title_text="Histogram where the buckets represent a bug detection rate for a LLM-based analysis and the count is the number of code artifacts in that bucket.",
        height=750,
        minreducedwidth=900,
        xaxis=dict(tickformat=".0%", title="Detection Rate (%)"),
        yaxis=dict(title="Number of Evaluated Code Artifacts"),
    )

    fig.write_html(output_path)

#def generate_pass_k_plot(csv_filepath: str, output_path: str):
#
#def generate_repair_summary_plot(csv_filepath: str, output_path: str):
#

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
        height=750,
        minreducedwidth=900,
        yaxis=dict(tickformat=".0%", title="Detection Rate (%)"),
        xaxis=dict(title="Date of Passing Commit"),
    )

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
        os.path.dirname(__file__), "../../assets/csv/detection_test_example.csv")
    rel_output_path = "../../assets/html/test_diff_bar_plot.html"
    output_path = os.path.join(
        os.path.dirname(__file__), rel_output_path) 
    comparison_method = "Diff"
    if len(sys.argv) > 1:
        output_path = os.path.abspath(sys.argv[1])
        if "diff" not in output_path:
            comparison_method = "Trace"
    generate_detection_bar_plot(csv_path, output_path, comparison_method)
