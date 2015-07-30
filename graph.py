import collections
import textwrap
import sys
import pygraphviz
import parser

import toolz
import pyrsistent
import json
import string

from pprint import pprint


Entity = collections.namedtuple("Entity", "id label cls")

attrs = {
        None : dict(),
        'inj' : dict(style="filled"),
        'obs' : dict(shape="plaintext"),
        'and' : dict(shape="ellipse")
      }

class Semantics(object):
    def __init__(self):
        self.i = 0
        self.nodes = set()
        self.edges = set()
        self.conflicts = set()
        self.letters = list(string.uppercase)

    def next_id(self):
        self.i += 1
        return '_%s' % self.i

    def conflict(self, ast):
        self.conflicts.add(tuple(ast))

    def label(self, ast):
        self.nodes.add(Entity(ast.id, "%s. %s" % (ast.id, textwrap.fill(ast.label, 30)), ast.cls))

    def relation(self, ast):
        if len(ast.source) == 1:
            self.edges.add((ast.source[0], ast.destination[0]))
        else:
            letter = self.next_id()
            self.nodes.add(Entity(letter, "AND", "and"))
            for s in ast.source:
                self.edges.add((s, letter))
            self.edges.add((letter, ast.destination[0]))

# imperative
def main(f):
    p = parser.thinkingprocessesParser()
    semantic_graph = Semantics()
    ast = p.parse(f.read(), rule_name="statements", semantics = semantic_graph)
    g = create_graph(semantic_graph)
    output(g)


# imperative
def output(g):
    print g

# pure
def create_graph(semantic_graph):
    g = pygraphviz.AGraph(directed=True, rankdir="BT")
    g.node_attr['shape'] = 'rectangle'
    g.node_attr['style'] = 'rounded'
    for identifier, label, cls in semantic_graph.nodes:
        g.add_node(identifier, label=label, **attrs[cls])
    g.add_edges_from(semantic_graph.edges)
    for a, b in semantic_graph.conflicts:
        g.add_edge(a, b, dir="none", constraint=False, color="red", penwidth=7)
    return g.to_string()

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        main(f)
