#!/usr/bin/env python3
import sys
from itertools import chain

from bnf import LLkRulesBuilder

VALID_MESSAGE = 'OK'
INVALID_MESSAGE = 'ERROR'

procedure_rules = '''
<procedure> ::= <procedure_heading>";" | <procedure_heading><parameters>";"
<procedure_heading> ::= "procedure"<identifier>
<parameters> ::= "("<parameter_list>")"
<parameter_list> ::= <parameter> | <parameter_list>";"<parameter>
<parameter> ::= <variable> | <typed_value_list>
<variable> ::= "var"<typed_value_list>
<typed_value_list> ::= <typed_value> | <typed_value_list>","<typed_value>
<typed_value> ::= <identifier_list>":"<type>
<identifier_list> ::= <identifier> | <identifier_list>","<identifier>
<identifier> ::= <letter> | <identifier><letter> | <identifier><digit>
<letter> ::= "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<type> ::= "char" | "boolean" | "integer" | "byte" | "shortint" | "smallint" | "word" | "longword" | "longint" | "int64" | "qword" | "cardinal" | "nativeint" | "nativeuint" | "real" | "real48" | "double" | "single" | "extended" | "comp" | "currency" | "string"
'''.split('\n')[-2:0:-1]

function_rules = '''
<function> ::= <function_heading>":"<type>";" | <function_heading><parameters>":"<type>";"
<function_heading> ::= "function"<identifier>
<parameters> ::= "("<parameter_list>")"
<parameter_list> ::= <parameter> | <parameter_list>";"<parameter>
<parameter> ::= <variable> | <typed_value_list>
<variable> ::= "var"<typed_value_list>
<typed_value_list> ::= <typed_value> | <typed_value_list>","<typed_value>
<typed_value> ::= <identifier_list>":"<type>
<identifier_list> ::= <identifier> | <identifier_list>","<identifier>
<identifier> ::= <letter> | <identifier><letter> | <identifier><digit>
<letter> ::= "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<type> ::= "char" | "boolean" | "integer" | "byte" | "shortint" | "smallint" | "word" | "longword" | "longint" | "int64" | "qword" | "cardinal" | "nativeint" | "nativeuint" | "real" | "real48" | "double" | "single" | "extended" | "comp" | "currency" | "string"
'''.split('\n')[-2:0:-1]


def create_rules():
    builder = LLkRulesBuilder()
    for rule_string in chain(procedure_rules, function_rules):
        builder.build_rule(rule_string.strip(), whitespace_insensitive=True, case_insensitive=True)

    return builder.get_rule('procedure'), builder.get_rule('function')


if __name__ == '__main__':
    procedure_rule, function_rule = create_rules()

    for line in sys.stdin:
        line = line.strip()
        if procedure_rule(line).is_valid() or function_rule(line).is_valid():
            print(VALID_MESSAGE)
        else:
            print(INVALID_MESSAGE)

