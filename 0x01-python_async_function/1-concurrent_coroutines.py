#!/usr/bin/env python3
""" Parallel execution of multiple coroutines
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Function to call multiple coroutines 'n' times and
        returns a list of delay time for each coroutine
        Args:
            n: iterations for coroutine
            max_delay: maximum delay time to await
                       coroutine
        Return: list of delay time for each coroutine
    """
    delay = await asyncio.gather(*(wait_random(max_delay)
                                 for _ in range(n)))
    return sorted(delay)
