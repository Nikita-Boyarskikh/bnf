from pytest import fixture

from bnf.test.fixtures.rules.common import rule_params, rule_ids


@fixture(params=rule_params, ids=rule_ids)
def llk_simple_recursive_rule(llk_simple_recursive_bnf, llk_rule_builder, request):
    return llk_rule_builder.build_rule(llk_simple_recursive_bnf, **request.param)


@fixture(params=rule_params, ids=rule_ids)
def llk_identifier_rule(llk_identifier_bnf, digits_bnf, letter_bnf, llk_rule_builder, request):
    llk_rule_builder.build_rule(digits_bnf)
    llk_rule_builder.build_rule(letter_bnf)
    return llk_rule_builder.build_rule(llk_identifier_bnf, **request.param)


@fixture(params=rule_params, ids=rule_ids)
def llk_identifier_list_rule(llk_identifier_bnf, digits_bnf, letter_bnf, llk_identifier_list_bnf, llk_rule_builder,
                             request):
    llk_rule_builder.build_rule(digits_bnf)
    llk_rule_builder.build_rule(letter_bnf)
    llk_rule_builder.build_rule(llk_identifier_bnf)
    return llk_rule_builder.build_rule(llk_identifier_list_bnf, **request.param)
