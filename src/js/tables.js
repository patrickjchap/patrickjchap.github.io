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

var data_example = text2CSV(syncFetch("/assets/csv/test_example.csv"));
console.log(data_example)
header = data_example.shift()

var bug_detection = $('#detectiontable').DataTable({
	columns: [
		{
			name: "tag",
			title: 'Artifact Image Tag',
		},
		{
			name: 'method',
			title: 'LLM-based Analysis',
		},
		{
			name: 'runs',
			title: 'Total Runs',
		},
		{
			title: 'Reports Matching Diff',
		},
		{
			title: 'Reports Matching Trace',
		},
		{
			name: 'time',
			title: 'Commit Fix Date',
		},
		{
			name: 'url',
			title: 'Diff URL',
			render: function(data, type, row, meta) {
				return '<a href="' + data + '">DIFF URL</a>';
			},
		},
	],
	data: data_example,
	rowsGroup: [// Always the array (!) of the column-selectors in specified order to which rows groupping is applied
				// (column-selector could be any of specified in https://datatables.net/reference/type/column-selector)
		'tag:name',
		'runs:name',
		'time:name',
		'url:name',
	],
})
