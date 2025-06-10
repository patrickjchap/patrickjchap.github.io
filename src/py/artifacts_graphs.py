import json
import os
import sys
from datetime import datetime
from itertools import cycle
import numpy as np
import argparse

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as io

from bugswarm.common.rest_api.database_api import DatabaseAPI

ARTIFACT_DATE_FORMAT = "%Y-%m-%d"
MODEL_DATE_FORMAT = "%Y-%m-%d"
palette = cycle(px.colors.qualitative.Plotly)
#palette = cycle(px.colors.sequential.PuBu)

def trunc_datetime(someDate):
    print(someDate)
    someDate = datetime.strptime(someDate, MODEL_DATE_FORMAT)
    return someDate.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

def generate_artifact_frequency_timeline(csv_filepath: str, models_filepath: str, output_path: str, api: DatabaseAPI):
    df = pd.read_csv(csv_filepath)
    print(df)
    df = df.sort_values(by="Fix Date")

    models_df = pd.read_csv(models_filepath)

    # Just using the CSV already created, kind of a hacky way to do things.
    # Create figure
    fig = go.Figure()
    fig.add_trace(
        go.Histogram(
            x=df["Fix Date"],
            xbins={
                "start": df["Fix Date"].min(),
                "end": df["Fix Date"].max(),
                "size": "M1",
            },
            showlegend=False,
            marker_color=next(palette),
        )
    )
    seen_dates = dict()
    for index, row in models_df.iterrows():
        cutoff_date = row["Cut-off Date"]
        if cutoff_date in seen_dates:
            seen_dates[cutoff_date].append(row["Model Name"])
            continue
        seen_dates[cutoff_date] = [row["Model Name"]]

    legend_names = dict()
    old_colors = dict()
    already_plotted = set()
    for index, row in models_df.iterrows():
        color = next(palette)
        cutoff_date = row["Cut-off Date"]
        if cutoff_date in already_plotted:
            continue
        already_plotted.add(cutoff_date)

        legend_name = row["Model Name"]
        if seen_dates[cutoff_date] != 1:
            legend_name = " & ".join([n for n in seen_dates[cutoff_date]])

        seen_dates[cutoff_date] = [row["Model Name"]]
        old_colors[cutoff_date] = color
        fig.add_vline(x=row["Cut-off Date"], line_dash="dash", line_color=color,showlegend=True, name=legend_name, line_width=3)
        legend_names[color] = row["Model Name"]


    # Set title
    fig.update_layout(
        title={
            "text":"Fix Dates for Null Pointer Dereference Evaluation Candidates over Time and LLM Knowledge Cutoff Dates.",
            "x": 0.5,
            "xanchor": "center"
        },
        height=600,
        width=1200,
        font=dict(size=16),
        #yaxis=dict(tickformat=".0%", title="Detection Rate (%)"),
        xaxis=dict(title="Time"),
        yaxis=dict(title="Number of Null Pointer Dereference Evaluation Candidates"),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
        ),
    )

    # Add range slider
#    fig.update_layout(
#        xaxis=dict(
#            rangeselector=dict(
#                buttons=list([
#                    dict(count=1,
#                         label="1m",
#                         step="month",
#                         stepmode="backward"),
#                    dict(count=6,
#                         label="6m",
#                         step="month",
#                         stepmode="backward"),
#                    dict(count=1,
#                         label="YTD",
#                         step="year",
#                         stepmode="todate"),
#                    dict(count=1,
#                         label="1y",
#                         step="year",
#                         stepmode="backward"),
#                    dict(step="all")
#                ])
#            ),
#            rangeslider=dict(
#                visible=True
#            ),
#            type="date"
#        )
#    )
#
    #fig.show()
    fig.write_html(output_path)
    fig.write_image("./testing.pdf")

def generate_artifact_timeline(csv_filepath: str, models_filepath: str, output_path: str):

    df = pd.read_csv(csv_filepath)
    df = df.sort_values(by="Fix Date")

    models_df = pd.read_csv(models_filepath)

    # Just using the CSV already created, kind of a hacky way to do things.
    # Create figure
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            name="NPEs in BugSwarm with LLM knowledge cutoff dates.",
            x=list(df["Fix Date"]),
            y=list(0.1 for _ in df["Fix Date"]),
            customdata=np.stack(
                (
                    df["Image Tag"],
                ),
                axis=1
            ),
            hovertemplate="<br>".join([
                "Commit Fix Date: %{x}",
                "Artifact Image Tag: %{customdata[0]}",
            ]),
            marker_color=next(palette),
            mode="markers",
            showlegend=False
        )
    )

    legend_names = dict()
    for index, row in models_df.iterrows():
        color = next(palette)
        fig.add_vline(x=row["Cut-off Date"], line_dash="dash", line_color=color,showlegend=True, name=row["Model Name"])
        legend_names[color] = row["Model Name"]


    # Set title
    fig.update_layout(
        title={
            "text":"Commit Dates for Fixes of BugSwarm Artifacts and LLM Knowledge Cutoff Dates.",
            "x": 0.5,
            "xanchor": "center"
        },
        height=680,
        width=1920,
        #yaxis=dict(tickformat=".0%", title="Detection Rate (%)"),
        xaxis=dict(title="Time"),
    )

    # Add range slider
    fig.update_layout(
        yaxis={
            "visible": False,
           # "showtick_labels": False,
            "range": [0.05, 0.15],
        },
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

    fig.show()
    fig.write_html(output_path)
    fig.write_image("./testing.png")


def _parse_args():
    parser = argparse.ArgumentParser(description="Script to generate plots for artifacts and models.")

    parser.add_argument(
        "-c", "--csv",
        default=os.path.join(
            os.path.dirname(__file__),
            "../../assets/csv/artifact-dates.csv"
        ),
        help="Path to bug detection CSV file.",
    )
    parser.add_argument(
        "-l", "--models",
        default=os.path.join(
            os.path.dirname(__file__),
            "../../assets/csv/models.csv"
        ),
        help="Path to bug detection CSV file.",
    )
    parser.add_argument(
        "-o", "--output",
        default=os.path.join(
            os.path.dirname(__file__),
            "../../assets/html/test_artifact_timeline.html",
        ),
        help="Output HTML path for generated plot.",
    )
    parser.add_argument(
        "-t", "--token",
        required=True)

    return parser.parse_args()

if __name__ == "__main__":
    args = _parse_args()
    csv_path = args.csv
    model_path = args.models
    output_path = os.path.abspath(args.output)
    api = DatabaseAPI(token=args.token)
    generate_artifact_frequency_timeline(csv_path, model_path, output_path, api)
