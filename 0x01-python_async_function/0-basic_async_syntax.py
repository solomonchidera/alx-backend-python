#!/usr/bin/env python3
import asyncio
import random

"""
Module Docs
0-basic_async_syntax
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Function Docs
    Generate a random delay time
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
