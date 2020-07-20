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

    git clone https://github.com/ryanfreckleton/thinkgraph
    cd thinkgraph
    pip install .

#### Hello World ####

Here's a basic use of thinkgraph to create an "evaporating cloud" diagram.

    # hello.tkg
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

thinkgraph uses a very simple language.
It is divided up into entities and relations.
An entity is any line of the form:

    <identifier>. <label>

Once you've created this file, running thinkgraph on it should generate a nice dot file.

     thinkgraph hello.tkg

Identifiers and Relations
-------------------------
Identifiers can be numbers, words, or letters.
Labels are ASCII sentences and continue until the end of the line.

Relations are how relationships between entities are graphed. The relationships are:

    <>  conflict
    ->  cause
    =>  feedback loop

Color/Styling
-------------
Styling of entities is determined by a code after the period.

    1.i An action
    2.o An obstacle
    3.g Something green
    4.r Something red
    5.y Something yellow


TODO
====
- Get it on PyPI
- Only use one "AND"
- Unit testing
- Refactoring/clean up code
- Handle unicode
- Use argparse
- Better styling
