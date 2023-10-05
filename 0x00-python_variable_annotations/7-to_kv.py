#!/usr/bin/env python3
'''7-to_kv
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    '''to_kv
    '''
    return (k, v**2)
