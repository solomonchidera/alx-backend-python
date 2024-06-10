#!/usr/bin/env python3
import asyncio
import heapq
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
"""
Module Docs
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function Docs
    """
    delays: List[float] = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay: float = await task
        heapq.heappush(delays, delay)

    sorted_delays: List[float] = [heapq.heappop(delays) for _ in range(
        len(delays))]
    return sorted_delays
