---
layout: default
---

{% tabs sections %}

{% tab sections About the Evaluation %}

{% endtab %}

{% tab sections Bug Detection Data %}

# Bug Detection

The task of bug detection involves running some analysis tool, either dynamic
or static, in order to automatically find bugs without having to rely on discovery
during user operation. For LLM-based approaches, these are typically done statically,
as the language model is taking in the source code directly as input with
the prompt. These approaches can range from relying entirely on a LLM to perform
the analysis, or may also take advantage of some traditional static analysis
to provide more relevant context to the model. For a deeper look at
background information about this task, please visit the
[background info]("/assets/pages/background.html") section of this site. The
particular types of bugs that we will be investigating approaches for currently
include:

<!--
* Null Pointer De-reference: When an attempt to access a pointer or object reference to a null value is made, e.g., Null Pointer Exceptions (NPE) in Java.
-->

Our evaluation on this task consists of running the LLM-based analyses on the
source code files provided in the artifact container that is maintained by
[BugSwarm](https://www.bugswarm.org). As the overwhelming majority of current
state-of-the-art language models are non-deterministic, we also run the analysis
approaches numerous times (in the current presented data, this number is X).
If the approach reports that a particular code snippet contains a bug, we
compare this snippet against the code contained in the diff of the fix and
the code contained in the buggy stack trace. If there is an overlap, we count
that bug as detected, keeping track of it is detected in the diff and stack
trace separately. This methodology was originally introduced in a paper by
[Tomassi et al.](https://web.cs.ucdavis.edu/~rubio/includes/ase21.pdf) The
final detection rate is the percentage of runs that detected a bug. For more
information on the specific of our methodology, please read further in the
[methodology]("/assets/pages/methodology.html") section of this site.

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

{% endtab %}

{% tab sections Program Repair Data %}

{% endtab %}

{% endtabs %}

