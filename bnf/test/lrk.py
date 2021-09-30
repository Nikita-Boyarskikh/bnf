from bnf.rule_parse_direction import RuleParseDirection


def test_direction(lrk_rule_builder):
    assert lrk_rule_builder.direction is RuleParseDirection.LEFT_TO_RIGHT
