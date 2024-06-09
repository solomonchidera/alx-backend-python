#!/usr/bin/env python3

"""
Module Docs
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function Docs
    """
    v = v ** 2
    return (k, v)
