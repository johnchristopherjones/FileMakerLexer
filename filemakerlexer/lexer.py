#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

class FileMakerLexer(RegexLexer):
    name = 'FileMaker'
    alias = 'fmcalc'
    filenames = ['*.fmcalc', '*.fmfn']
    _name = r'[^\,\+\-\*\/\^\&\=\≠\>\<\(\)\[\]\{\}\"\;\:\$]+'

    flags = re.DOTALL | re.UNICODE | re.MULTILINE

    tokens = {
        'commentsandwhitespace':[
            (r'\s+', Text),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline)
        ],
        'constant': [
            # Constants
            (r'"(\\\\|\\"|[^"])*"', String, ('#pop', 'operator')),
            (u'¶', String, ('#pop', 'operator')),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?', Number, ('#pop', 'operator'))
        ],
        'variable': [
            (r'\$\$' + _name, Name.Variable.Global, ('#pop', 'operator')),
            (r'\$' + _name, Name.Variable, ('#pop', 'operator')),
            (_name, Name.Variable.Instance, ('#pop', 'operator')),
        ],
        'field': [
            (_name + r'::' + _name, Name, ('#pop', 'operator'))
        ],
        'function': [
            (r'(' + _name + ')\s*(\(\s*)',
                bygroups(Name.Function, Name.Punctuation), 'expression'),
            (r'\)', Name.Punctuation, ('#pop', 'operator'))
        ],
        'list': [
            (r'\[', Name.Punctuation, 'expression'),
            (r';', Punctuation, ('#pop', 'expression')),
        ],
        'expression': [
            include('commentsandwhitespace'),
            include('function'),
            include('field'),
            include('constant'),
            include('variable'),
            include('list'),
            (r'\(', Name.Punctuation, 'expression'),
        ],
        'operator': [
            include('commentsandwhitespace'),
            (r'[*+-/&^=<>]|not|and|or', Operator, ('#pop', 'expression')),
            (u'≠|≤|≥', Operator, ('#pop', 'expression')),
            # Saw end of expression (function or group) instead
            (r'\)', Name.Punctuation, ('#pop', 'operator')),
            (r'\]', Name.Punctuation, ('#pop', 'operator')),
            (r';', Name.Punctuation, ('#pop', 'expression')),
        ],
        'root': [
            (r'\[', Error),
            include('expression')
        ]
    }
