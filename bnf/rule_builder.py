import re

from typing import List, Iterable

from .regexps import RULE_NTS_WRAPPER_RE, RULE_DEFINITION_SEP, RULE_OR_OP
from .rule import Rule, RecursiveRuleCall
from .rule_parse_direction import RuleParseDirection
from .utils import throw

# Error messages
INVALID_RULE_NAME_MESSAGE = 'Invalid rule name: \'{}\''
INVALID_TS_FORMAT_MESSAGE = 'Invalid rule format (must be <name> or "term"): \'{}\''
RULE_UNDEFINED_MESSAGE = 'The rule <{}> is not defined! It must be defined below <{}> rule'


class RuleBuilderError(Exception):
    """
    TODO
    """
    pass


class UndefinedRuleError(RuleBuilderError):
    """
    TODO
    """
    pass


class InvalidRuleNameError(RuleBuilderError):
    """
    TODO
    """
    pass


class InvalidTSFormatError(RuleBuilderError):
    """
    TODO
    """
    pass


class RulesBuilder(object):
    """
    TODO
    RulesBuilder - class, realized builder for creates rules set from BNF.
    """

    direction: RuleParseDirection = None

    def __init__(self, rules=None):
        assert self.direction is not None
        self.rules = rules or {}
        self.rule_nt_re = re.compile(RULE_NTS_WRAPPER_RE)

    def build_rule(self, rule_string, overwrite_if_exists=False, whitespace_insensitive=False, case_insensitive=False):
        """
        TODO
        """
        rule_name, rule_definition = rule_string.split(RULE_DEFINITION_SEP, 1)
        rule_name = self._build_rule_name(rule_name.strip())

        if not overwrite_if_exists and self.rules.get(rule_name, None) is not None:
            return self.rules[rule_name]
        self.rules[rule_name] = RecursiveRuleCall()

        try:
            rule_definition = self._build_rule_definition(rule_definition.strip())
        except UndefinedRuleError as ex:
            raise UndefinedRuleError(RULE_UNDEFINED_MESSAGE.format(*ex.args, rule_name))

        rule = Rule(rule_name, rule_definition, self.direction,
                    whitespace_insensitive=whitespace_insensitive, case_insensitive=case_insensitive)
        self.rules[rule_name] = rule
        return rule

    def _build_rule_name(self, rule_name):
        ex = InvalidRuleNameError(INVALID_RULE_NAME_MESSAGE.format(rule_name))
        search = re.search(self.rule_nt_re, rule_name) or throw(ex)
        (search.group(0) == rule_name) or throw(ex)
        return search.group(1)

    def _build_rule_definition(self, rule_definition):
        nts_stub = '<NTS>'

        nt_names = re.findall(self.rule_nt_re, rule_definition)
        nt_names.reverse()  # For use nts.pop() later

        nts = []
        for nt_name in nt_names:
            rule = self.rules.get(nt_name, None) or throw(UndefinedRuleError(nt_name))
            nts.append(rule)

        definition = []
        rule_conditions = rule_definition.split(RULE_OR_OP)
        for condition in rule_conditions:
            condition = re.sub(self.rule_nt_re, nts_stub, condition)
            rules = iter(condition.split(nts_stub))

            res = [next(rules)]
            for rule in rules:
                res.extend((nts.pop(), rule))

            res = [rule for rule in res if rule != '']
            res = self._fix_str_rules(res)
            definition.append(res[::self.direction.value])

        return definition

    @staticmethod
    def _fix_str_rules(rules):
        result = []
        for rule in rules:
            if isinstance(rule, str):
                rule = rule.strip()
                re.search('^["\']', rule) and re.search('["\']$', rule)\
                    or throw(InvalidTSFormatError(INVALID_TS_FORMAT_MESSAGE.format(rule)))
                rule = re.sub('^["\']', '', rule)
                rule = re.sub('["\']$', '', rule)
            result.append(rule)
        return result

    def add_rule(self, rule):
        """
        TODO
        """
        assert isinstance(rule, Rule)
        self.rules[rule.name] = rule
        return self

    def get_rule(self, name):
        """
        TODO
        """
        return self.rules.get(name, None)

    def __repr__(self):
        return '{}(rules=[{}])'.format(self.__class__.__name__, ','.join(self.rules.keys()))


class LLkRulesBuilder(RulesBuilder):
    """
    TODO
    """
    direction = RuleParseDirection.RIGHT_TO_LEFT


class LRkRulesBuilder(RulesBuilder):
    """
    TODO
    """
    direction = RuleParseDirection.LEFT_TO_RIGHT
