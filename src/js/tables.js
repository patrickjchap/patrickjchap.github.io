var data_example = [
	[
		"1c-syntax-bsl-language-server-32438380396",
		"Baseline",
		"20",
		"13/20 (65.00%)",
		"16/20 (80.00%)",
		"2018-08-10T16:21:24Z",
		"https://www.bugswarm.org/diffs/1c-syntax-bsl-language-server-32438378016",
	],
	[
		"1c-syntax-bsl-language-server-32438380396",
		"Data-Flow",
		"20",
		"14/20 (70.00%)",
		"16/20 (80.00%)",
		"2018-08-10T16:21:24Z",
		"https://www.bugswarm.org/diffs/1c-syntax-bsl-language-server-32438378016",
	],
	[
		"1c-syntax-bsl-language-server-32438380396",
		"Chain-of-Thought",
		"20",
		"15/20 (75.00%)",
		"18/20 (90.00%)",
		"2018-08-10T16:21:24Z",
		"https://www.bugswarm.org/diffs/1c-syntax-bsl-language-server-32438378016",
	],
	[
		"2c-syntax-bsl-language-server-32438380396",
		"Baseline",
		"20",
		"13/20 (65.00%)",
		"16/20 (80.00%)",
		"2015-08-10T16:21:24Z",
		"https://www.bugswarm.org/diffs/2c-syntax-bsl-language-server-32438378016",
	],
	[
		"2c-syntax-bsl-language-server-32438380396",
		"Data-Flow",
		"20",
		"14/20 (70.00%)",
		"16/20 (80.00%)",
		"2015-08-10T16:21:24Z",
		"https://www.bugswarm.org/diffs/2c-syntax-bsl-language-server-32438378016",
	],
	[
		"2c-syntax-bsl-language-server-32438380396",
		"Chain-of-Thought",
		"20",
		"15/20 (75.00%)",
		"18/20 (90.00%)",
		"2015-08-10T16:21:24Z",
		"https://www.bugswarm.org/diffs/2c-syntax-bsl-language-server-32438378016",
	],
	[
		"3c-syntax-bsl-language-server-32438380396",
		"Baseline",
		"20",
		"13/20 (65.00%)",
		"20/20 (80.00%)",
		"2022-08-10T16:21:24Z",
		"https://www.bugswarm.org/diffs/3c-syntax-bsl-language-server-32438378016",
	],
	[
		"3c-syntax-bsl-language-server-32438380396",
		"Data-Flow",
		"20",
		"14/20 (70.00%)",
		"20/20 (80.00%)", "2022-08-10T16:21:24Z",
		"https://www.bugswarm.org/diffs/3c-syntax-bsl-language-server-32438378016",
	],
	[
		"3c-syntax-bsl-language-server-32438380396",
		"Chain-of-Thought",
		"20",
		"15/20 (75.00%)",
		"18/20 (90.00%)",
		"2022-08-10T16:21:24Z",
		"https://www.bugswarm.org/diffs/3c-syntax-bsl-language-server-32438378016",
	],
]

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
