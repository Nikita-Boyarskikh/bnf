from typing import List, Callable, Union, Iterable, Iterator
from itertools import tee

from .regexps import RULE_OR_OP, RULE_DEFINITION_SEP
from .rule_parse_direction import RuleParseDirection
from .utils import not_none_filter

RuleLambdaReturnType = Iterable[str]
RuleLambdaType = Callable[[str], RuleLambdaReturnType]
RuleDefinitionType = List[List[Union[str, RuleLambdaType]]]


class RecursiveRuleCall(object):
    """
    TODO
    """
    pass


class RecursiveRuleWrongPlace(Exception):
    """
    TODO
    """
    pass


class RuleResult(object):
    def __init__(self, iterable: Iterator):
        self.iterable = iterable

    def __iter__(self):
        return iter(self.iterable)

    def __next__(self):
        return next(self.iterable)

    def __len__(self):
        self.iterable, test = tee(self.iterable)
        return sum(1 for _ in test)

    def is_valid(self):
        return any(x == '' for x in self.iterable)


class Rule(object):
    """
    TODO
    """
    def __init__(self, name: str, definition: RuleDefinitionType, direction: RuleParseDirection,
                 whitespace_insensitive=False, case_insensitive=False):
        self.name = name
        self.definition = definition  # Used only for repr to save string values of terms
        self.parsed_definition = []
        self.direction = direction
        self.whitespace_insensitive = whitespace_insensitive
        self.case_insensitive = case_insensitive

        for condition in definition:
            conditions = []
            for i, token in enumerate(condition):
                if i != len(condition) - 1 and isinstance(token, RecursiveRuleCall):
                    raise RecursiveRuleWrongPlace()
                if not isinstance(token, RecursiveRuleCall) and not callable(token):
                    token = self._get_token_lambda(token)
                conditions.append(token)
            self.parsed_definition.append(conditions)

    def _get_token_lambda(self, token: str) -> RuleLambdaType:
        """
        TODO
        """
        def token_lambda(x: str) -> RuleLambdaReturnType:
            closure = token
            if self.whitespace_insensitive:
                x = x.strip()
            if self.case_insensitive:
                x = x.lower()
                closure = closure.lower()
            check_condition = x.startswith if self.direction is RuleParseDirection.LEFT_TO_RIGHT else x.endswith
            return not_none_filter(
                (self._get_part_of_token(closure, x) if check_condition(closure) else None,)
            )
        return token_lambda

    def __call__(self, token: str) -> RuleResult:
        """
        TODO
        """
        variants = ()
        for condition in self.parsed_definition:
            if self.whitespace_insensitive:
                token = token.strip()
            intermediate_result = (token,)
            for subcondition in condition:
                if isinstance(subcondition, RecursiveRuleCall):
                    subcondition = Rule(self.name, self.definition, self.direction,
                                        self.whitespace_insensitive, self.case_insensitive)
                result = ()
                for res in intermediate_result:
                    result = tuple(result) + tuple(subcondition(res))
                intermediate_result = tuple(result)
            variants = variants + intermediate_result
        return RuleResult(variants)

    def _get_part_of_token(self, part: str, token: str) -> str:
        if len(part) == 0:
            return token
        return token[len(part):] if self.direction is RuleParseDirection.LEFT_TO_RIGHT else token[:-len(part)]

    def __repr__(self) -> str:
        rule_reprs = []
        for rule_items in self.definition:
            rule_item_reprs = []
            for rule in rule_items[::self.direction.value]:
                if isinstance(rule, Rule):
                    rule_item_reprs.append('<{}>'.format(rule.name))
                else:
                    rule_item_reprs.append('"{}"'.format(str(rule)))
            rule_reprs.append(' '.join(rule_item_reprs))
        return '<{}> {} {}'.format(self.name, RULE_DEFINITION_SEP, RULE_OR_OP.join(rule_reprs))
