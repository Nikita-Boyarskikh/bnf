from typing import Iterator

from bnf.rule import Rule


def assert_all_tests_is_valid(rule: Rule, tests: Iterator[str]):
    assert all([rule(i).is_valid() for i in tests])
