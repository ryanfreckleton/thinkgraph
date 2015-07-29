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
        'inj' : dict(style="rounded,filled"),
        'obs' : dict(shape="plaintext"),
        'and' : dict(shape="ellipse")
      }

class Semantics(object):
    def __init__(self):
        self.nodes = set()
        self.edges = set()
        self.letters = list(string.uppercase)

    def label(self, ast):
        self.nodes.add(Entity(ast.id, ast.label, ast.cls))

    def relation(self, ast):
        if len(ast.source) == 1:
            self.edges.add((ast.source[0], ast.destination[0]))
        else:
            letter = self.letters.pop(0)
            self.nodes.add(Entity(letter, "AND", "and"))
            for s in ast.source:
                self.edges.add((s, letter))
            self.edges.add((letter, ast.destination[0]))

# imperative
def main(f):
    p = parser.thinkingprocessesParser()
    semantic_graph = Semantics()
    ast = p.parse(f.read(), rule_name="statements", semantics = semantic_graph)
    g = create_graph(semantic_graph.nodes, semantic_graph.edges)
    output(g)


# imperative
def output(g):
    print g

# pure
def create_graph(labels, edges):
    g = pygraphviz.AGraph(directed=True, rankdir="TB")
    g.node_attr['shape'] = 'rectangle'
    for identifier, label, cls in labels:
        g.add_node(identifier, label=label, **attrs[cls])
    g.add_edges_from(edges)
    return g.to_string()

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        main(f)
