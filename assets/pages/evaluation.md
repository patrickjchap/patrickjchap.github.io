---
layout: default
---

{% tabs sections %}

{% tab sections About the Evaluation %}

To demonstrate our LLM evaluation framework, we measure the performance of
various LLM-based approaches performing the task of bug detection and program
repair. For the presented evaluation, we select real-world bugs from open-source
projects that have been mined via BugSwarm. Specifically, we select source
code artifacts that contain null pointer dereference bugs in Java and type
errors in Python. We are able to select these code artifacts automatically,
as BugSwarm automatically tracks the types of Exceptions and Errors that occur
during executing the various tests that are ran through the project's 
continous integration (CI) pipeline.

`Example of potential null pointer dereference bug when dealing with inheritance.`
```java
class Superclass {
  protect String data;

  public void processData() {
    System.out.println(data.toUpperCase()); // NPE if data is uninitialized!
  }
}

class Subclass extends Superclass {
  public Subclass (String value) {
    super();
    this.data = value;
    processData();
  }
}
```

For **bug detection**, there is a high-likelihood that many bug report warnings
are generated that are unrelated to the particular bug-of-interest that is
reported in the stack trace. To determine if a particular report is related to
the bug in the stack trace, we leverage two techniques originally introduced
by [Tomassi et al.](https://ieeexplore.ieee.org/document/9678535): (1) checking
against the code diff and (2) checking against the stack trace. That is, if a
particular bug report overlaps with the code diff or stack trace, then we count
that bug as detected. In the case of using the code diff, this can represent
an over-approximation of the expected performance, as code diffs often contain
compeletely unrelated code. On the other hand, using the stack trace can often
be an under-approximation, as null pointers relating to external factors like
I/O may not be captured.

In regards to **program repair**, we task the LLM with fixing the bug in the
source code artifact. We feed the source code file from the buggy version
of the source code artifact to the LLM, asking for a patch to fix the bug. We
compare this fix against the code diff that causes the subsequent passing code
artifact to pass CI. In our case, we capture the CodeBLEU metric, but can also
capture the pass@k metric as well. One of the major advantages that we have
in leveraging BugSwarm is that we obtain an environment that is reproducible.
This means that can apply the patch automatically and run the unit tests to
check if they pass. 

If you wish to read more on the specific methodology on how we each part of
the evaluation framework runs, please visit the
[methodology](/assets/pages/methodology.html) section.

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

