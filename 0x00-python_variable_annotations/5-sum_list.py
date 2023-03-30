#!/usr/bin/env python3
'''type-annotated sum_list function'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' returns sum of list with floating-point elements'''
    return sum(input_list)
