---
layout: default
---
# Evaluating Bug Detection on NPEs

This page presents the experimental results for evaluating LLM-based bug detectors
on finding NPE bugs. To read more about the dataset that the evaluation is ran
on, please visit the [dataset](/assets/pages/dataset.html) page.

There are two primary presented metrics `Detect@k` and the `detection rate`. The
detection rate is simply the number of bug detector runs that successfully found
the bug divided by the total number of runs. This is of course averaged over the
total number of times the detector was ran and over all benchmarks evaluated on.
The `detect@k` is based on the `pass@k` metric that gives the probability that at
least one in `k` bug detector runs will successfully find the bug. This metric
is calculated as:
\\(Detect@k = \mathbb{E} [1 - \frac{\binom{n-c}{k}}{\binom{n}{k}}]\\)

Where \\(n\\) is the total number of samples, \\(c\\) are the number of correct
samples, \\(k\\) is the number of samples considered for the calculation. We also
ensure that \\(n \ge k\\).

### Evaluated Approaches for LLM-based Bug Detection

For the particular LLM-based approaches that we evaluate, we select four:

**BaseBUGS**: Simply asks the LLM for any detected bugs in the analyzed code. 

**BaseNPE**: Simply asks the LLM for any NPEs in the analyzed code.

**Dataflow**: Frames the problem as a dataflow analysis and asks the LLM for
any dataflow sources, sinks, sanitizers, unsanitized dataflow, and violations
of the null check. This will then ask if any locations in code can possibly
have an NPE.

**CWE**: Based on the [Common Weakness Enumerations](https://cwe.mitre.org/) that
provides the given description from the CWE page.

**NCR**: I.e., Null Call Returns. This first performs an initial analysis that
asks the LLM if any functions in the analyzed files may possibly return NULL. The
given list of NULL returning functions is then supplied as additional context when
finding bugs.

We also include results with and without **chain-of-thought** context as is noted
in the experimental results tables.

## Plots

{% tabs dplots %}

{% tab dplots Detect@k Bar Plot - Code Diff %}

<html> 
  <head> 
    <script> 
    $(function(){
      $("#includedContentDetectKBarDiff").load("/assets/html/test_diff_detect_k_bar_plot.html"); 
    });
    </script> 
  </head> 

  <body> 
     <div id="includedContentDetectKBarDiff"></div>
  </body> 
</html>

{% endtab %}

{% tab dplots Detect@k Bar Plot - Stack Trace %}

<html> 
  <head> 
    <script> 
    $(function(){
      $("#includedContentDetectKBarTrace").load("/assets/html/test_trace_detect_k_bar_plot.html"); 
    });
    </script> 
  </head> 

  <body> 
     <div id="includedContentDetectKBarTrace"></div>
  </body> 
</html>

{% endtab %}

{% tab dplots Detection Rate Histogram - Code Diff %}

<html> 
  <head> 
    <script> 
    $(function(){
      $("#includedContentDetectionHistDiff").load("/assets/html/test_diff_histogram.html"); 
    });
    </script> 
  </head> 

  <body> 
     <div id="includedContentDetectionHistDiff"></div>
  </body> 
</html>


{% endtab %}

{% tab dplots Detection Rate Histogram - Stack Trace %}

<html> 
  <head> 
    <script> 
    $(function(){
      $("#includedContentDetectionHistTrace").load("/assets/html/test_trace_histogram.html"); 
    });
    </script> 
  </head> 

  <body> 
     <div id="includedContentDetectionHistTrace"></div>
  </body> 
</html>

{% endtab %}


{% tab dplots Detection Rate Bar Plot - Code Diff %}

<html> 
  <head> 
    <script> 
    $(function(){
      $("#includedContentDetectionBarDiff").load("/assets/html/test_diff_bar_plot.html"); 
    });
    </script> 
  </head> 

  <body> 
     <div id="includedContentDetectionBarDiff"></div>
  </body> 
</html>

{% endtab %}

{% tab dplots Detection Rate Bar Plot - Stack Trace %}

<html> 
  <head> 
    <script> 
    $(function(){
      $("#includedContentDetectionBarTrace").load("/assets/html/test_trace_bar_plot.html"); 
    });
    </script> 
  </head> 

  <body> 
     <div id="includedContentDetectionBarTrace"></div>
  </body> 
</html>

{% endtab %}

{% endtabs %}

## Experimental Results

<table id="detectiontable" class="display"></table>

<script src="/src/js/evaluation_detection.js"></script>


