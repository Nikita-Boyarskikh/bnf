from pytest import fixture


@fixture
def simple_optional_bnf():
    return '<simple_optional> ::= "" | "a"'


@fixture
def digits_bnf():
    from string import digits
    return '<digit> ::= "{}"'.format('" | "'.join(tuple(digits)))


@fixture
def letter_bnf():
    from string import ascii_lowercase
    return '<letter> ::= "{}"'.format('" | "'.join(tuple(ascii_lowercase)))


@fixture
def type_bnf():
    return '<type> ::= "char" | "boolean" | "integer" | "byte" | "shortint" | "smallint" | "word" | "longword" | ' \
           '"longint" | "int64" | "qword" | "cardinal" | "nativeint" | "nativeuint" | "real" | "real48" | "double" | ' \
           '"single" | "extended" | "comp" | "currency" | "string"'
