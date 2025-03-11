# Methodology

Traditional static analyzers have been used to automatically detect potential
bugs in source code such as [NullAway](https://github.com/uber/NullAway) 
and [SpotBugs](https://spotbugs.github.io/). Static analyzers, while frequently
used with great success in real world software development, often have various
limitations. For example, it is often the case that the formal reasoning applied
to learn program semantics relies on approximations. Otherwise, exhaustively
learning all relevant program facts can require running the program itself to
explore all paths.

## Null Pointer De-reference Detection

A particular bug of interest that is often targeted by static analyzers is
null pointer de-reference bugs, i.e., null pointer exceptions (NPE) in Java.
These bugs occur when a piece of code unintentionally de-references a null
pointer, usually performing an action such as calling a method when the object
is set to NULL. Various approaches have demonstrated some success in detecting
these types of bugs, but as demonstrated in a study by [Tomassi et al.](https://web.cs.ucdavis.edu/~rubio/includes/ase21.pdf),
these tools suffer from both a significant number of false positives and the majority
number of real NPE bugs being missed.

As such, there have been several approaches introduced that leverage both features
of traditional static analyzers and LLMs to improve bug finding capabilities. Since
our evaluation of LLM-based approaches is agnostic to a particular framework, we
can compare any number of LLM-based approaches as long as the bug reports are
parseable. For NPEs, we take a look at four particular methodologies that have
been introduced in other works:

1. Baseline: Includes a prompt that asks the language model to report the code
   snippets that introduce a null pointer de-reference bug.
2. Data-flow: This prompt is constructed by introducing the problem as a data-flow
   analysis. The agent is tasked with providing learned facts such as data-flow,
   sanitizers, and data sanitization. This is then used to report particular
   code snippets where null pointers are improperly sanitized, i.e. checked. 
3. Chain-of-Thought: Leverages the specific CWE provided description of a
   null pointer de-reference, as well as several chain-of-thought demonstrative
   exemplars.
4. Chain-of-Thought with Call Graph: Similar to the previous example, except
   also calculates the program-under-analysis' call graph before running the
   NPE bug detection. Based on the previous analysis runs, the result can then
   be fed to the LLM as context in the prompt. In the context of NPE detection,
   this can help indicate what other function calls may unsanitized.


