from pytest import fixture


@fixture
def llk_simple_recursive_bnf():
    return '<simple_recursive> ::= "a" | <simple_recursive>"a"'


@fixture
def llk_identifier_bnf():
    return '<identifier> ::= <letter> | <identifier><letter> | <identifier><digit>'


@fixture
def llk_identifier_list_bnf():
    return '<identifier_list> ::= <identifier> | <identifier_list>","<identifier>'
