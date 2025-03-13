---
layout: default
---

{% tabs sections %}

{% tab sections About the Evaluation %}

The evaluation results presented here are for the task of bug detection.

## Bug Detection

For background information on the task of bug detection, please visit the
[background](/assets/pages/background.html) section of the site. The source
code files that are analyzed by the evaluated approaches are obtained from
the source code artifacts that are provided by the BugSwarm framework. For
more information on how BugSwarm and these code artifacts are used in our
evaluation framework, please visit the [methodology](/assets/pages/methodology.html)
section of the site.



{% endtab %}

{% tab sections Bug Detection Data %}

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

{% endtab %}

{% tab sections Program Repair Data %}

{% endtab %}

{% endtabs %}

