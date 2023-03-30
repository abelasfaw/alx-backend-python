#!/usr/bin/env python3
'''type-annotated sum_mixed_list function'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    ''' returns sum of list with floating-point or int elements'''
    return float(sum(mxd_lst))
