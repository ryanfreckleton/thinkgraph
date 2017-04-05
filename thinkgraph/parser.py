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

from grako.buffering import Buffer
from grako.parsing import graken, Parser
from grako.util import re, RE_FLAGS, generic_main  # noqa


KEYWORDS = {}


class thinkingprocessesBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        namechars='',
        **kwargs
    ):
        super(thinkingprocessesBuffer, self).__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs
        )


class thinkingprocessesParser(Parser):
    def __init__(
        self,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        left_recursion=False,
        parseinfo=True,
        keywords=None,
        namechars='',
        buffer_class=thinkingprocessesBuffer,
        **kwargs
    ):
        if keywords is None:
            keywords = KEYWORDS
        super(thinkingprocessesParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            parseinfo=parseinfo,
            keywords=keywords,
            namechars=namechars,
            buffer_class=buffer_class,
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
                    self._loop_()
                with self._option():
                    self._conflict_()
                self._error('no available options')
        self._positive_closure(block0)
        self._check_eof()

    @graken()
    def _label_(self):
        self._identifier_()
        self.name_last_node('id')
        with self._group():
            with self._choice():
                with self._option():
                    self._token('.')
                    self._CLASS_()
                    self.name_last_node('cls')
                with self._option():
                    self._token('.')
                self._error('expecting one of: .')
        self._string_()
        self.name_last_node('label')
        self.ast._define(
            ['cls', 'id', 'label'],
            []
        )

    @graken()
    def _relation_(self):
        self._and_stmt_()
        self.name_last_node('source')
        self._token('->')
        self._identifier_()
        self.name_last_node('destination')
        self._NEWLINE_()
        self.ast._define(
            ['destination', 'source'],
            []
        )

    @graken()
    def _loop_(self):
        self._and_stmt_()
        self.name_last_node('source')
        self._token('=>')
        self._identifier_()
        self.name_last_node('destination')
        self._NEWLINE_()
        self.ast._define(
            ['destination', 'source'],
            []
        )

    @graken()
    def _and_stmt_(self):
        self._identifier_()
        self.add_last_node_to_name('@')

        def block1():
            self._token('and')
            self._identifier_()
            self.add_last_node_to_name('@')
        self._closure(block1)

    @graken()
    def _conflict_(self):
        self._identifier_()
        self.add_last_node_to_name('@')
        self._token('<>')
        self._identifier_()
        self.add_last_node_to_name('@')
        self._NEWLINE_()

    @graken()
    def _identifier_(self):
        self._pattern(r'\w+')

    @graken()
    def _string_(self):
        self._pattern(r'.*')

    @graken()
    def _NEWLINE_(self):
        self._pattern(r'\r?\n')

    @graken()
    def _CLASS_(self):
        with self._choice():
            with self._option():
                self._token('inj')
            with self._option():
                self._token('obs')
            with self._option():
                self._token('red')
            with self._option():
                self._token('green')
            self._error('expecting one of: green inj obs red')


class thinkingprocessesSemantics(object):
    def statements(self, ast):
        return ast

    def label(self, ast):
        return ast

    def relation(self, ast):
        return ast

    def loop(self, ast):
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


def main(filename, startrule, **kwargs):
    with open(filename) as f:
        text = f.read()
    parser = thinkingprocessesParser()
    return parser.parse(text, startrule, filename=filename, **kwargs)


if __name__ == '__main__':
    import json
    from grako.util import asjson

    ast = generic_main(main, thinkingprocessesParser, name='thinkingprocesses')
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(asjson(ast), indent=2))
    print()
