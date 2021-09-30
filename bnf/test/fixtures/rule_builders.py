from pytest import fixture

from bnf import LLkRulesBuilder, LRkRulesBuilder


@fixture
def llk_rule_builder():
    return LLkRulesBuilder()


@fixture
def lrk_rule_builder():
    return LRkRulesBuilder()


@fixture(params=[llk_rule_builder, lrk_rule_builder], ids=['llk', 'lrk'])
def rule_builder(request):
    return request.param()
