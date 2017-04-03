thinkgraph: Theory of Constraints Thinking Processes Graphing Tool
==================================================================
This a tool that has a mini-language to help with creating diagrams ala Theory
of Constraints Thinking Processes.
- List
- Connections
- Styling

Usage
-----
#### Installation ####

  pip install toc

#### Hello World ####

Here's a basic use of graphthink to create an "evaporating cloud" diagram.

  1. Try new things
  2. Don't try new things
  3. We must be satisfied
  4. We must be secure
  5. Happiness

  1 <> 2
  1 -> 3
  2 -> 4
  3 -> 5
  4 -> 5

graphthink uses a very simple language.
It is divided up into entities and relations.
An entity is any line of the form:

    <identifier>. <label>

Identifiers and Relations
-------------------------
Identifiers can be numbers, words, or letters.
Labels are ASCII sentences and continue until the end of the line.

Relations are how relationships between entiteis are graphed. The relationships are:

  <>  conflict
  ->  cause
  =>  feedback loop

Color/Styling
-------------
Styling of entitites is determined by a code after the period.

  1.inj An action
  2.obs An obstacle
  3.green Something green (and good)
  4.red Something red and (bad)


TODO
====
- PyPI
- Only use one "AND"
- Unit testing
- Refactoring/clean up code
- Handle unicode
- Use argparse
- Better styling
