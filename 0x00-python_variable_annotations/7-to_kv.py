#!/usr/bin/env python3
'''type-annotated to_kv function'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' returns a tuple with k as 1st and square of v as 2nd element'''
    return (k, float(v * v))
