from .utils import assert_all_tests_is_valid


def test_build_twice(digits_bnf, rule_builder):
    fake_digits = '<digit> ::= ""'
    digits = rule_builder.build_rule(digits_bnf)
    digits2 = rule_builder.build_rule(fake_digits)
    assert digits == digits2


def test_simple_optional(simple_optional_rule):
    tests = ['a', '']
    assert_all_tests_is_valid(simple_optional_rule, tests)


def test_case_insensitive(type_rule):
    tests = ['Char', 'INTEGER', 'string', 'ReAl48', 'currency', 'nAtIVEuINT']
    results = [type_rule(i).is_valid() for i in tests]
    if type_rule.case_insensitive:
        assert all(results)
    else:
        assert results[4]
        assert results[2]
        assert not any([results[0], results[1], results[3], results[5]])


def test_whitespace_sensitive(letter_rule):
    tests = [' a ', ' a', ' a', 'a']
    results = [letter_rule(i).is_valid() for i in tests]
    if letter_rule.whitespace_insensitive:
        assert all(results)
    else:
        assert results[-1]
        assert not any([results[0], results[1], results[2]])


def test_build_digit(digits_rule):
    tests = (str(i) for i in range(10))
    assert_all_tests_is_valid(digits_rule, tests)


def test_build_types(type_rule):
    tests = 'char integer real48 string'.split()
    assert_all_tests_is_valid(type_rule, tests)


# TODO add_rule
# TODO get_rule
# TODO repr
# TODO test RuleResult
# TODO exceptions
# TODO typing RuleBuilder
