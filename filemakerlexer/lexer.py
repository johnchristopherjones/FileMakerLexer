#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

class FileMakerLexer(RegexLexer):
    name = 'FileMaker'
    alias = 'fmcalc'
    filenames = ['*.fmcalc', '*.fmfn']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'//.*?\n', Comment.Single),
            (r'/(\\\n)?[*](.|\n)*?[*](\\\n)?/', Comment.Multiline),

            # Constants
            (r'"(\\\\|\\"|[^"])*"', String),
            (r'[¶]', String),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?', Number.Float),

            # Grouping
            (r'\(|\)', Punctuation),

            # Function/builtins
            (r'(\w+)\s*?(\()',
                bygroups(Name.Function, Name.Keyword)),

            # Operators
            (r'[*+-/&^=≠<>≤≥]|not|and|or', Operator),
            (r'\[', Keyword),
            (r'(\])\s*(\))',
                bygroups(Keyword, Name.Keyword)),
            (r'(\])\s*(;)',
                bygroups(Keyword, Name.Keyword)),

            # Variable
            (r'$$[^\,\+\-\*\/\^\&\=\≠\>\<\(\)\[\]\{\}\"\;\:\$]+', Name.Variable.Global),
            (r'$[^\,\+\-\*\/\^\&\=\≠\>\<\(\)\[\]\{\}\"\;\:\$]+', Name.Variable),
            (r'[^\,\+\-\*\/\^\&\=\≠\>\<\(\)\[\]\{\}\"\;\:\$]+', Name.Variable.Instance),

            # Operators
            (r'[*+-/&^=≠<>≤≥]|not|and|or', Operator),
            (r';', Punctuation)
        ],
    }
