---
layout: default
---

# Bug Detection

## Plots

{% tabs plots %}

{% tab plots Time Series Detection Rate - Code Diff %}

<html> 
  <head> 
    <script> 
    $(function(){
      $("#includedContentDiff").load("/assets/html/test_diff_timeline.html"); 
    });
    </script> 
  </head> 

  <body> 
     <div id="includedContentDiff"></div>
  </body> 
</html>


{% endtab %}

{% tab plots Time Series Detection Rate - Stack Trace %}

<html> 
  <head> 
    <script> 
    $(function(){
      $("#includedContentTrace").load("/assets/html/test_trace_timeline.html"); 
    });
    </script> 
  </head> 

  <body> 
     <div id="includedContentTrace"></div>
  </body> 
</html>

{% endtab %}

{% endtabs %}

### Table Data 

<table id="detectiontable" class="display"></table>
<!--
<label for="before">Before date filter:</label>
<input
  type="date"
  id="before"
  name="filter-before"
  value="2030-12-31"
  min="2000-01-01"
  max="2030-12-31" />

<label for="after">After date filter:</label>
<input
  type="date"
  id="after"
  name="filter-after"
  value="2000-01-01"
  min="2000-01-01"
  max="2030-12-31" />


{% tabs method %}

{% tab method Baseline %}

<table id="detectiontable" class="display"></table>

/*<table id="table" class="display">
 <thead>
    <tr>
        <th> Artifact Image Tag </th>
        <th> LLM-based Analysis </th>
        <th> Total Runs </th>
        <th> Reports Matching Diff </th>
        <th> Reports Matching Trace </th>
        <th> Commit Fix Date </th>
        <th> Diff URL </th>
    </tr>
  </thead>

  <tbody>
    <tr>
        <td rowspan=3>1c-syntax-bsl-language-server-32438380396</td>
        <td>Baseline</td>
        <td rowspan=3>20</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
		<td rowspan=3> 2015-08-10T16:21:24Z </td>
        <td rowspan=3>https://www.bugswarm.org/diffs/1c-syntax-bsl-language-server-32438378016</td>
    </tr>
    <tr>
        <td>Data-Flow</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
    </tr>
    <tr>
        <td>Chain-of-Thought</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
    </tr>
    <tr>
        <td rowspan=3>2c-syntax-bsl-language-server-32438380396</td>
        <td>Baseline</td>
        <td rowspan=3>20</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
		<td rowspan=3> 2015-08-10T16:21:24Z </td>
        <td rowspan=3>https://www.bugswarm.org/diffs/1c-syntax-bsl-language-server-32438378016</td>
    </tr>
    <tr>
        <td>Data-Flow</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
    </tr>
    <tr>
        <td>Chain-of-Thought</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
    </tr>
    <tr>
        <td rowspan=3>3c-syntax-bsl-language-server-32438380396</td>
        <td>Baseline</td>
        <td rowspan=3>20</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
		<td rowspan=3> 2015-08-10T16:21:24Z </td>
        <td rowspan=3>https://www.bugswarm.org/diffs/1c-syntax-bsl-language-server-32438378016</td>
    </tr>
    <tr>
        <td>Data-Flow</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
    </tr>
    <tr>
        <td>Chain-of-Thought</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
    </tr>
    <tr>
        <td rowspan=3>4c-syntax-bsl-language-server-32438380396</td>
        <td>Baseline</td>
        <td rowspan=3>20</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
		<td rowspan=3> 2015-08-10T16:21:24Z </td>
        <td rowspan=3>https://www.bugswarm.org/diffs/1c-syntax-bsl-language-server-32438378016</td>
    </tr>
    <tr>
        <td>Data-Flow</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
    </tr>
    <tr>
        <td>Chain-of-Thought</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
    </tr>
    <tr>
        <td rowspan=3>1c-syntax-bsl-language-server-32438380396</td>
        <td>Baseline</td>
        <td rowspan=3>20</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
		<td rowspan=3> 2015-08-10T16:21:24Z </td>
        <td rowspan=3>https://www.bugswarm.org/diffs/1c-syntax-bsl-language-server-32438378016</td>
    </tr>
    <tr>
        <td>Data-Flow</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
    </tr>
    <tr>
        <td>Chain-of-Thought</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
    </tr>

    <tr>
        <td rowspan=3>1c-syntax-bsl-language-server-32438380396</td>
        <td>Baseline</td>
        <td rowspan=3>20</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
		<td rowspan=3> 2015-08-10T16:21:24Z </td>
        <td rowspan=3>https://www.bugswarm.org/diffs/1c-syntax-bsl-language-server-32438378016</td>
    </tr>
    <tr>
        <td>Data-Flow</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
    </tr>
    <tr>
        <td>Chain-of-Thought</td>
        <td>13/20 (65.00%)</td>
        <td>16/20 (80.00%)</td>
    </tr>
 
  </tbody>
</table>

{% endtab %}

{% tab method Data-Flow Prompt %}
{% endtab %}

{% tab method Chain-of-Thought %}
{% endtab %}

{% endtabs %}
-->
