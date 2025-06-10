---
layout: default 
---

<img src="/assets/images/workflow.png" alt="">
<figcaption>Fig. 1: The workflow for evaluating LLM-based bug detectors.</figcaption>

With the explosion of popularity among the various code large language models
(LLM), there have been numerous techniques introduced to automatically perform
software development tasks such as bug finding and fixing. Many of the
well-established benchmarks for evaluating code LLMs are based on small-scale
problem solving starting from scratch, similar to what one might see in a
technical coding interview. These of course can be beneficial into providing
insight as to the LLMs reasoning capabilities, but have several potential
shortcomings such as often being static and not involving real-world software
systems.

Many of the available LLMs do not make the entirety of their training set
available, meaning that there are often no guarantees as to what a model may have
knowledge of. It may the case that certain samples from a benchmark may be
either used as training data, either directly or indirectly. There have been
efforts to overcome this problem by crafting examples that are newer than the
given LLM's training knowledge cutoff date, but as newer iterations of these
models are made available, the knowledge cutoff date may advance. 

It is also the case that a lot of the popular benchmarks that exist are not
representative of real software. This has been addressed by several other
works, e.g., leveraging real-world bug datasets, but these still suffer from
the issue of the datasets being static.

We attempt to address some of these concerns by introducing our framework
for performing lifelong evaluations of large language models. In particular,
we evaluate LLM-based approaches in performing both bug detection and
program repair. We leverage the BugSwarm framework to select relevant code
artifacts that contain real-world buggy and fixed versions of open-source code
projects. BugSwarm is beneficial, as it contains a myriad of artifacts already
available for evaluation, but can also be used to mine newer repositories on
GitHub. This means that we can contiously extract real-world artifacts that
contain bugs that we can use to evaluate LLM-based approaches. We can then
compare the relative performance of the LLMs and check their performance comparing
the commit fix date against the LLM training cutoff date.

In the [background](/assets/pages/background.html) section of this site we
provide preliminary information on various metrics used, current evaluation
strategies, bug detection, program repair, and BugSwarm. In our [methodology](/assets/pages/methodology.html)
section, we provide the workflow of our approach and explain how evaluation is
performed. We then provide some evaluation results on various LLM-based approaches
using our evaluation framework in the [detection evaluation](/assets/pages/evaluation_detection.html)
and [repair evaluation](/assets/pages/evaluation_repair.html) sections. Finally,
our [related works](/assets/pages/related.html) section provides related research
into this area.
