#!/usr/bin/env python3
"""
Module Docs
"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function Docs
    """
    delay = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delay)
