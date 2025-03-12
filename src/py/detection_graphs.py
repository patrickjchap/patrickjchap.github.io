import json
import os
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

def generate_detection_rate_timeline(csv_filepath: str, output_path: str):
	df = pd.read_csv(csv_filepath)
	df = df.sort_values(by="Commit Fix Date")

	# Create figure
	fig = go.Figure()

	methods_to_plot = set(list(df["Methodology"]))
	for method in methods_to_plot:
		selected_df = df[df["Methodology"] == method]
		print(selected_df)
		fig.add_trace(
			go.Scatter(
                name=method,
                x=list(selected_df["Commit Fix Date"]),
                y=list(selected_df["Reports in Diff"]),
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
					"URL: %{customdata[2]}",
				]),
                marker_color=next(palette)))

	# Set title
	fig.update_layout(
		title_text="Time series with buggy code artifacts and detection rates."
	)
	fig.update_traces(
		hovertemplate="<br>".join([
			"Commit Fix Date: %{x}",
			"Detection Rate: %{y}",
			"Artifact Image Tag: %{customdata[0]}",
			"Times Ran: %{customdata[1]}",
			"URL: %{customdata[2]}",
		])
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
		os.path.dirname(__file__), "../../assets/csv/test_example.csv")
	output_path = os.path.join(
		os.path.dirname(__file__), "../../assets/html/test_timeline.html")
	generate_detection_rate_timeline(csv_path, output_path)
