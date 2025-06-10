function syncFetch(path) {
	const request = new XMLHttpRequest();
	request.open("GET", path, false); // `false` makes the request synchronous
	request.send(null);

	if (request.status === 200) {
	  return request.responseText;
	}
	return null;
}

function text2CSV(text) {
  const lines = text.split('\n').filter(line => line.trim() !== "");
  return lines.map(line => line.split(','));
}

var data_example = text2CSV(syncFetch("/assets/csv/detection_results.csv"));
console.log(data_example)
header = data_example.shift()

var bug_detection = $('#detectiontable').DataTable({
	columns: [
		{
			name: "tag",
			title: 'Artifact Image Tag',
		},
        {
			name: 'url',
			title: 'Diff URL',
			render: function(data, type, row, meta) {
				return '<a href="' + data + '" target="_blank"> Diff URL </a>';
			},
		},
		{
			name: 'time',
			title: 'Commit Fix Date',
		},
		{
			name: 'runs',
			title: 'Total Runs',
		},
        {
			name: 'llm',
			title: 'Selected LLM',
		},
        {
			name: 'knowledge',
			title: 'LLM Knowledge Cutoff Date',
		},
		{
			name: 'method',
			title: 'Detection Method',
		},
		{
			title: 'Detection Rate - Diff',
		},
		{
			title: 'Detection Rate - Trace',
		},
        {
            name: 'llmout',
            title: 'Example Bug Report'
	    //  render: function(data, type, row, meta) {
		//		return '<a href="' + data + '" target="_blank"> Output </a>';
		//	},
        },
	],
	data: data_example,
	rowsGroup: [// Always the array (!) of the column-selectors in specified order to which rows groupping is applied
				// (column-selector could be any of specified in https://datatables.net/reference/type/column-selector)
		'tag:name',
		'url:name',
		'time:name',
		'runs:name',
        'llm:name',
		'knowledge:name',
	],
    // There are three models that run 10 times over all benchmarks, so 30 per benchmark.
    // This value should be a multiple of 30.
    pageLength: 90,
});
