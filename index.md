---
layout: default 
---

With the ever increasing demand for large language models (LLM) to be streamlined
into the software development cycle, there have been numerous approaches that
explore areas such as bug detection and program repair. Traditional approaches
incorporate various static analyses or leverage verification techniques to
accomplish these tasks. However, these methods are often based on approximations
about program behavior or only applicable to certain programming patterns. The
development of these tools can often take considerable effort as well to model
the problem. These challenges have motivated the use of LLMs to assist in these
tasks, as the starting cost of incorporating an already existing language model
to analyze source code is low while also being the case that the LLM itself is
agnostic to any particular programming pattern.

While it is an exciting time to explore the various use cases that these LLMs

This site presents the data and methodology for our work on the lifelong
evaluation of large language models (LLM). In particular, this work demonstrates
the evaluation of code LLMs performing tasks such as bug detection and program
repair on real-world code artifacts. These code artifacts are continuously mined
using the [BugSwarm](https://www.bugswarm.org) framework, which allows us to select
code artifacts that demonstrate various types of bugs. BugSwarm is especially useful
because these code artifacts are mined in pass and failing pairs, providing
relevant data such as code diffs that enable our evaluation to compare bug
reports and suggested patches from any LLM-based technique.

[Bug Detection](/assets/pages/bug_detection.md)
