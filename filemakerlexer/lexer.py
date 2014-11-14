#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

__all__ = ['FileMakerLexer']

class FileMakerLexer(RegexLexer):
    name = 'FileMaker'
    aliases = ['fmcalc', 'fmfn', 'filemaker']
    filenames = ['*.fmcalc', '*.fmfn']
    flags = re.DOTALL | re.UNICODE | re.MULTILINE
    _name = r'[^\,\+\-\*\/\^\&\=\≠\>\<\(\)\[\]\{\}\"\;\:\$\s]+\s*'
    # Keyword and builtin lists for FMP13 from (GPL v3)
    # https://github.com/DonovanChan/Filemaker.tmbundle/blob/master/Syntaxes/FileMaker.tmLanguage
    _builtins = (r'\b(Average|Count|List|Max|Min|StDev|StDevP|Sum|Variance|'
        r'VarianceP|Date|Day|DayName|DayNameJ|DayOfWeek|DayOfYear|'
        r'Month|MonthName|MonthNameJ|WeekOfYear|WeekOfYearFiscal|Year|'
        r'YearName|DatabaseNames|FieldBounds|FieldComment|FieldIDs|'
        r'FieldNames|FieldRepetitions|FieldStyle|FieldType|'
        r'GetNextSerialValue|LayoutIDs|LayoutNames|LayoutObjectNames|'
        r'RelationInfo|ScriptIDs|ScriptNames|TableIDs|TableNames|'
        r'ValueListIDs|ValueListItems|ValueListNames|WindowNames|'
        r'External|FV|NPV|PMT|PV|Case|Choose|Evaluate|EvaluationError|'
        r'GetAsBoolean|GetField|GetFieldName|GetLayoutObjectAttribute|'
        r'GetNthRecord|If|IsEmpty|IsValid|IsValidExpression|Let|Lookup|'
        r'LookupNext|Self|Abs|Ceiling|Combination|Div|Exp|Factorial|'
        r'Floor|Int|Lg|Ln|Log|Mod|Random|Round|SetPrecision|Sign|Sqrt|'
        r'Truncate|Extend|GetRepetition|Last|GetSummary|Char|Code|'
        r'Exact|Filter|FilterValues|GetAsCSS|GetAsDate|GetAsNumber|'
        r'GetAsSVG|GetAsText|GetAsTime|GetAsTimestamp|GetAsURLEncoded|'
        r'GetValue|Hiragana|KanaHankaku|KanaZenkaku|KanjiNumeral|'
        r'Katakana|Left|LeftValues|LeftWords|Length|Lower|Middle|'
        r'MiddleValues|MiddleWords|NumToJText|PatternCount|Position|'
        r'Proper|Quote|Replace|Right|RightValues|RightWords|'
        r'RomanHankaku|RomanZenkaku|SerialIncrement|Substitute|Trim|'
        r'TrimAll|Upper|ValueCount|WordCount|RGB|TextColor|'
        r'TextColorRemove|TextFont|TextFontRemove|TextFormatRemove|'
        r'TextSize|TextSizeRemove|TextStyleAdd|TextStyleRemove|Hour|'
        r'Minute|Seconds|Time|Timestamp|Acos|Asin|Atan|Cos|Degrees|'
        r'Pi|Radians|Sin|Tan|Get|GetHeight|GetThumbnail|GetWidth|'
        r'VerifyContainer|ExecuteSQL|Location|LocationValues|'
        r'Base64Decode|Base64Encode|CurrentTimeUTCMilliseconds)\b')
    _constants = (r'(?i)\b(AccountName|ActiveFieldContents|ActiveFieldName|'
        r'ActiveFieldTableName|ActiveLayoutObjectName|'
        r'ActiveModifierKeys|ActiveRepetitionNumber|ActiveSelectionSize|'
        r'ActiveSelectionStart|AllowAbortState|AllowToolbarState|'
        r'ApplicationLanguage|ApplicationVersion|'
        r'CalculationRepetitionNumber|CurrentDate|CurrentHostTimestamp|'
        r'CurrentTime|CurrentTimestamp|CustomMenuSetName|DesktopPath|'
        r'DocumentsPath|DocumentsPathListing|ErrorCaptureState|'
        r'ExtendedPrivileges|FileMakerPath|FileName|FilePath|FileSize|'
        r'FoundCount|HighContrastColor|HighContrastState|'
        r'HostApplicationVersion|HostIPAddress|HostName|LastError|'
        r'LastMessageChoice|LastODBCError|LayoutAccess|LayoutCount|'
        r'LayoutName|LayoutNumber|LayoutTableName|LayoutViewState|'
        r'MultiUserState|NetworkProtocol|PageNumber|PortalRowNumber|'
        r'PreferencesPath|PrinterName|PrivilegeSetName|RecordAccess|'
        r'RecordID|RecordModificationCount|RecordNumber|RecordOpenCount|'
        r'RecordOpenState|RequestCount|RequestOmitState|ScreenDepth|'
        r'ScreenHeight|ScreenWidth|ScriptName|ScriptParameter|'
        r'ScriptResult|SortState|StatusAreaState|SystemDrive|'
        r'SystemIPAddress|SystemLanguage|SystemNICAddress|SystemPlatform|'
        r'SystemVersion|TemporaryPath|TextRulerVisible|TotalRecordCount|'
        r'TriggerKeystroke|TriggerModifierKeys|UserCount|UserName|'
        r'UseSystemFormatsState|WindowContentHeight|WindowContentWidth|'
        r'WindowDesktopHeight|WindowDesktopWidth|WindowHeight|WindowLeft|'
        r'WindowMode|WindowName|WindowTop|WindowVisible|WindowWidth|'
        r'WindowZoomLevel|Roman|Greek|Cryllic|CentralEurope|ShiftJIS|'
        r'TraditionalChinese|SimplifiedChinese|OEM|Symbol|Other|Plain|'
        r'Bold|Italic|Underline|Condense|Extend|Strikethrough|SmallCaps|'
        r'Superscript|Subscript|Uppercase|Lowercase|Titlecase|'
        r'WordUnderline|DoubleUnderline|AllStyles|objectType|hasFocus|'
        r'containsFocus|isFrontTabPanel|bounds|left|right|top|bottom|'
        r'width|height|rotation|startPoint|endPoint|source|content|'
        r'enclosingObject|containedObjects|ConnectionState|'
        r'InstalledFMPlugins|PersistentID|UUID|WindowStyle|'
        r'ConnectionAttributes|ContainerAttribute|Device|EncryptionState|'
        r'ModifiedFields|NetworkType|ScriptAnimationState|'
        r'TriggerGestureInfo|WindowOrientation)\b')

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
        'builtin': [
            (r'Self', Name.Builtin.Pseudo, ('#pop', 'operator')),
            (r'(?i)\bTrue|False\b', Name.Constant, ('#pop', 'operator')),
            (_builtins, Name.Builtin, ('#pop', 'expression')),
            (_constants, Name.Constant, ('#pop', 'operator')),
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
            (r'(' + _name + ')\s*(\()',
                bygroups(Name.Function, Punctuation), 'expression'),
            (r'\)', Punctuation, ('#pop', 'operator'))
        ],
        'list': [
            (r'\[', Punctuation, 'expression'),
            (r';', Punctuation, ('#pop', 'expression')),
        ],
        'expression': [
            include('commentsandwhitespace'),
            (r'not', Operator.Word),
            include('builtin'),
            include('function'),
            include('field'),
            include('constant'),
            include('variable'),
            include('list'),
            (r'\(', Punctuation, 'expression'),
        ],
        'operator': [
            include('commentsandwhitespace'),
            (r'[*+-/&^=<>]', Operator, ('#pop', 'expression')),
            (r'not|and|or', Operator.Word, ('#pop', 'expression')),
            (u'≠|≤|≥', Operator, ('#pop', 'expression')),
            # Saw end of expression (function or group) instead
            (r'\)', Punctuation),
            (r'\]', Punctuation),
            (r';', Punctuation, ('#pop', 'expression')),
            # Whitespace is allowed in a variable or function name
            (_name, Name.Variable.Instance, ('#pop', 'operator')),
        ],
        'root': [
            (r'\[', Error),
            include('expression')
        ]
    }
