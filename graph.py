#!/usr/bin/env python

import collections
import textwrap
import sys
import pygraphviz
import parser

Entity = collections.namedtuple("Entity", "id label cls")

attrs = {
        None : dict(),
        'and' : dict(shape="ellipse", style=""),
        'inj' : dict(style="filled", fillcolor='#B3CDE3'),
        'obs' : dict(shape="plaintext", fillcolor="transparent"),
        'red' : dict(style="rounded,filled", fillcolor="#FBB4AE"),
        'green' : dict(style="rounded,filled", fillcolor="#CCEBC5"),
      }

class Semantics(object):
    def __init__(self):
        self.i = 0
        self.nodes = set()
        self.edges = set()
        self.and_edges = set()
        self.loop_edges = set()
        self.and_loop_edges = set()
        self.conflicts = set()

    def next_id(self):
        self.i += 1
        return '_%s' % self.i

    def conflict(self, ast):
        self.conflicts.add(tuple(ast))

    def label(self, ast):
        label = "%s. %s" % (ast.id, textwrap.fill(ast.label, 30))
        self.nodes.add(Entity(ast.id, label, ast.cls))

    def relation(self, ast):
        if len(ast.source) == 1:
            self.edges.add((ast.source[0], ast.destination))
        else:
            node_id = self.next_id()
            self.nodes.add(Entity(node_id, "AND", "and"))
            for s in ast.source:
                self.and_edges.add((s, node_id))
            self.edges.add((node_id, ast.destination))

    def loop(self, ast):
        if len(ast.source) == 1:
            self.loop_edges.add((ast.source[0], ast.destination))
        else:
            node_id = self.next_id()
            self.nodes.add(Entity(node_id, "AND", "and"))
            for s in ast.source:
                self.and_loop_edges.add((s, node_id))
            self.edges.add((node_id, ast.destination))

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
    g.node_attr['style'] = 'rounded,filled'
    g.node_attr['fillcolor'] = '#FFFFCC'
    for identifier, label, cls in semantic_graph.nodes:
        g.add_node(identifier, label=label, **attrs[cls])
    g.add_edges_from(semantic_graph.edges)
    g.add_edges_from(semantic_graph.and_edges, dir="none")
    g.add_edges_from(semantic_graph.loop_edges, constraint=False)
    g.add_edges_from(semantic_graph.and_loop_edges, dir="none", constraint=False)
    for a, b in semantic_graph.conflicts:
        g.add_edge(a, b, style="tapered", dir="both", arrowhead=None,
                  arrowtail=None, constraint=False, color="red", penwidth=7)
        g.add_subgraph([a,b], rank="same")
    return g.to_string()

if __name__ == "__main__":
    if not sys.argv[1:]:
        main(sys.stdin)
    else:
        with open(sys.argv[1]) as f:
            main(f)
