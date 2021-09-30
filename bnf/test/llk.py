from bnf.rule_parse_direction import RuleParseDirection

from .utils import assert_all_tests_is_valid


def test_direction(llk_rule_builder):
    assert llk_rule_builder.direction is RuleParseDirection.RIGHT_TO_LEFT


def test_simple_recursion(llk_simple_recursive_rule):
    tests = ['a', 'aaaaa', 'a'*10]
    assert_all_tests_is_valid(llk_simple_recursive_rule, tests)


def test_build_identifier(llk_identifier_rule):
    tests = ['abc', 'abf34', 's34fsf3', 'a']
    assert_all_tests_is_valid(llk_identifier_rule, tests)


def test_build_identifier_list(llk_identifier_list_rule):
    tests = ['abc,abf34,s34fsf3,a']
    assert_all_tests_is_valid(llk_identifier_list_rule, tests)
