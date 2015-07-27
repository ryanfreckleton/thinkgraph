import textwrap
import sys
import pygraphviz

with open(sys.argv[1]) as f:
    g = pygraphviz.AGraph()
    g.node_attr['shape'] = 'rectangle'
    for num, line in enumerate(f, start=1):
        g.add_node(num, label=textwrap.fill(line.strip(), width=30))

print g
