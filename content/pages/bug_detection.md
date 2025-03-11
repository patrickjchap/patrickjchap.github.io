---
layout: default
title: Evaluation - Bug Detection
---

# LLELLM: Bug Detection

## Plots

{% tabs log %}

{% tab log Detection Rate - Code Diff %}
```php
var_dump('hello');
```
{% endtab %}

{% tab log Detection Rate - Stack Trace %}
```javascript
console.log('hello');
```
{% endtab %}

{% tab log Total Reports %}
```javascript
pputs 'hello'
```
{% endtab %}

{% endtabs %}

### Second tabs

{% tabs method %}

{% tab method Baseline %}

<table>
 <thead>
    <tr>
        <th> Artifact Image Tag </th>
        <th> LLM-based Analysis </th>
        <th> Total Runs </th>
        <th> Reports Matching Diff </th>
        <th> Reports Matching Trace </th>
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
<table>

{% endtab %}

{% tab method Data-Flow Prompt %}
{% endtab %}

{% tab method Chain-of-Thought %}
{% endtab %}

{% endtabs %}
