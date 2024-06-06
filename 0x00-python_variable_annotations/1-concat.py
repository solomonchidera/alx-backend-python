#!/usr/bin/env python3
"""
1-concat.py

Function that takes two string and returns the concatenated version

Function:
- concat string1 and string2 that gets concatenated and returns the result
"""


def concat(string1: str, string2: str) -> str:
    """
    Concatenates two strings and returns the result.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return f'{string1}' + f'{string2}'
