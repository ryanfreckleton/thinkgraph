import collections
import textwrap
import sys
import pygraphviz

import toolz
import pyrsistent


Entity = collections.namedtuple("Entity", "id label")
islabel_line = lambda s: '.' in s

class Node(pyrsistent.PClass):
    attributes = pyrsistent.field()
    children = pyrsistent.field()

    def to_graphviz(self):
        raise NotImplementedError

class Groups(object):
    def __init__(self, f):
        self.groups = toolz.groupby(islabel_line, f)

    def label_lines(self):
        return self.groups[True]

    def edge_lines(self):
        return self.groups[False]

def get_nodes(edge_lines):
    nodes = []
    for el in edge_lines:
        if el.strip():
            nodes.append(el.strip().split('->'))
    return nodes

def get_edges(nodes):
    edges = []
    for n in nodes:
        edges.extend(zip(map(str.strip, n), map(str.strip, n[1:])))
    return edges

# imperative
def main(f):
    groups = Groups(f)
    nodes = get_nodes(groups.edge_lines())
    edges = get_edges(nodes)
    labels = get_labels(groups.label_lines())
    g = create_graph(labels, edges)
    output(g)


def get_labels(lines):
    return (get_entity(line) for line in lines)

# imperative
def output(g):
    print g

# pure
def get_entity(line):
    identifier, label = line.split('.', 1)
    label = textwrap.fill(label.strip(), width=30)
    return Entity(identifier, label)

# pure
def create_graph(labels, edges):
    g = pygraphviz.AGraph(directed=True, rankdir="TB")
    g.node_attr['shape'] = 'rectangle'
    for identifier, label in labels:
        g.add_node(identifier, label=label)
    g.add_edges_from(edges)
    return g.to_string()

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        main(f)
