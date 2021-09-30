from typing import Iterable, TypeVar, Optional

T = TypeVar('T')


def throw(ex):
    raise ex


def not_none_filter(iterable: Iterable[Optional[T]]) -> Iterable[T]:
    return filter(lambda x: x is not None, iterable)
