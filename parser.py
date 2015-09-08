#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

from grako.parsing import graken, Parser
from grako.util import re, RE_FLAGS


__version__ = (2015, 9, 4, 3, 9, 17, 4)

__all__ = [
    'thinkingprocessesParser',
    'thinkingprocessesSemantics',
    'main'
]


class thinkingprocessesParser(Parser):
    def __init__(self, whitespace=None, nameguard=None, **kwargs):
        super(thinkingprocessesParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=None,
            eol_comments_re=None,
            ignorecase=None,
            **kwargs
        )

    @graken()
    def _statements_(self):

        def block0():
            with self._choice():
                with self._option():
                    self._label_()
                with self._option():
                    self._relation_()
                with self._option():
                    self._conflict_()
                self._error('no available options')
        self._positive_closure(block0)

        self._check_eof()

    @graken()
    def _label_(self):
        self._identifier_()
        self.ast['id'] = self.last_node
        with self._group():
            with self._choice():
                with self._option():
                    self._token('.')
                    self._CLASS_()
                    self.ast['cls'] = self.last_node
                with self._option():
                    self._token('.')
                self._error('expecting one of: .')
        self._string_()
        self.ast['label'] = self.last_node

        self.ast._define(
            ['id', 'cls', 'label'],
            []
        )

    @graken()
    def _relation_(self):
        self._and_stmt_()
        self.ast['source'] = self.last_node
        self._token('->')
        self._identifier_()
        self.ast['destination'] = self.last_node
        self._NEWLINE_()

        self.ast._define(
            ['source', 'destination'],
            []
        )

    @graken()
    def _and_stmt_(self):
        self._identifier_()
        self.ast.setlist('@', self.last_node)

        def block1():
            self._token('and')
            self._identifier_()
            self.ast.setlist('@', self.last_node)
        self._closure(block1)

    @graken()
    def _conflict_(self):
        self._identifier_()
        self.ast.setlist('@', self.last_node)
        self._token('<>')
        self._identifier_()
        self.ast.setlist('@', self.last_node)
        self._NEWLINE_()

    @graken()
    def _identifier_(self):
        self._pattern(r'\w+')

    @graken()
    def _string_(self):
        self._pattern(r'.*')

    @graken()
    def _NEWLINE_(self):
        self._pattern(r'\n')

    @graken()
    def _CLASS_(self):
        with self._choice():
            with self._option():
                self._token('inj')
            with self._option():
                self._token('obs')
            with self._option():
                self._token('red')
            self._error('expecting one of: inj obs red')


class thinkingprocessesSemantics(object):
    def statements(self, ast):
        return ast

    def label(self, ast):
        return ast

    def relation(self, ast):
        return ast

    def and_stmt(self, ast):
        return ast

    def conflict(self, ast):
        return ast

    def identifier(self, ast):
        return ast

    def string(self, ast):
        return ast

    def NEWLINE(self, ast):
        return ast

    def CLASS(self, ast):
        return ast


def main(filename, startrule, trace=False, whitespace=None, nameguard=None):
    import json
    with open(filename) as f:
        text = f.read()
    parser = thinkingprocessesParser(parseinfo=False)
    ast = parser.parse(
        text,
        startrule,
        filename=filename,
        trace=trace,
        whitespace=whitespace,
        nameguard=nameguard)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import argparse
    import string
    import sys

    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in thinkingprocessesParser.rule_list():
                print(r)
            print()
            sys.exit(0)

    parser = argparse.ArgumentParser(description="Simple parser for thinkingprocesses.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-n', '--no-nameguard', action='store_true',
                        dest='no_nameguard',
                        help="disable the 'nameguard' feature")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('-w', '--whitespace', type=str, default=string.whitespace,
                        help="whitespace specification")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(
        args.file,
        args.startrule,
        trace=args.trace,
        whitespace=args.whitespace,
        nameguard=not args.no_nameguard
    )

