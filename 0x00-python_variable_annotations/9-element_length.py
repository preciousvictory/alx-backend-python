#!/usr/bin/env python3
'''9-element_length
'''
from typing import Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> Tuple[Sequence, int]:
    '''element_length
    '''
    return [(i, len(i)) for i in lst]
