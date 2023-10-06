#!/usr/bin/env python3
'''101-safely_get_value
'''
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')
dft = Union[T, None]
Rtn = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: dft = None) -> Rtn:
    '''safely_get_value
    '''
    if key in dct:
        return dct[key]
    else:
        return default
