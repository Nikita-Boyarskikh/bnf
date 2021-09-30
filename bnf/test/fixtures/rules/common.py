from pytest import fixture

rule_params = [
    {},
    {'case_insensitive': True},
    {'whitespace_insensitive': True},
    {'case_insensitive': True, 'whitespace_insensitive': True},
]
rule_ids = [','.join(param.keys()) for param in rule_params]


@fixture(params=rule_params, ids=rule_ids)
def simple_optional_rule(simple_optional_bnf, rule_builder, request):
    return rule_builder.build_rule(simple_optional_bnf, **request.param)


@fixture(params=rule_params, ids=rule_ids)
def type_rule(type_bnf, rule_builder, request):
    return rule_builder.build_rule(type_bnf, **request.param)


@fixture(params=rule_params, ids=rule_ids)
def digits_rule(digits_bnf, rule_builder, request):
    return rule_builder.build_rule(digits_bnf, **request.param)


@fixture(params=rule_params, ids=rule_ids)
def letter_rule(letter_bnf, rule_builder, request):
    return rule_builder.build_rule(letter_bnf, **request.param)
