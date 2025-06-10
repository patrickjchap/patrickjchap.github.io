function reloadDetectKBarPlotTraceHTML(ele, html_path) {
  $("#includedContentDetectKBarTrace").load("/assets/html/test_trace_detect_k_bar_plot.html"); 
}
function reloadDetectKBarPlotDiffHTML(ele, html_path) {
  $("#includedContentDetectKBarDiff").load("/assets/html/test_diff_detect_k_bar_plot.html"); 
}
function reloadDetectionBarPlotTraceHTML(ele, html_path) {
  $("#includedContentDetectionBarTrace").load("/assets/html/test_trace_bar_plot.html"); 
}
function reloadDetectionBarPlotDiffHTML(ele, html_path) {
  $("#includedContentDetectionBarDiff").load("/assets/html/test_diff_bar_plot.html"); 
}
function reloadDetectionHistogramTraceHTML(ele, html_path) {
  $("#includedContentDetectionHistTrace").load("/assets/html/test_trace_histogram.html"); 
}
function reloadDetectionHistogramDiffHTML(ele, html_path) {
  $("#includedContentDetectionHistDiff").load("/assets/html/test_diff_histogram.html"); 
}

$("#dplots-detect-k-bar-plot---code-diff")[0].addEventListener(
	"click",
	reloadDetectKBarPlotDiffHTML
);
$("#dplots-detect-k-bar-plot---stack-trace")[0].addEventListener(
	"click",
	reloadDetectKBarPlotTraceHTML
);
$("#dplots-detection-rate-bar-plot---code-diff")[0].addEventListener(
	"click",
	reloadDetectionBarPlotDiffHTML
);
$("#dplots-detection-rate-plot---stack-trace")[0].addEventListener(
	"click",
	reloadDetectionBarPlotTraceHTML
);
$("#dplots-detection-rate-histogram---code-diff")[0].addEventListener(
	"click",
	reloadDetectionHistogramDiffHTML
);
$("#dplots-detection-rate-histogram---stack-trace")[0].addEventListener(
	"click",
	reloadDetectionHistogramTraceHTML
);
