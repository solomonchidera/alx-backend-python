#!/usr/bin/env python3
import asyncio
import random

"""
Module Docs
"""


asyn def wait_random(max_delay: int = 10) -> float:
    """
    Function Docs
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
