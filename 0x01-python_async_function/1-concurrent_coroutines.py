#!/usr/bin/env python3
'''
implementing wait_n coroutine
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''funct returns list of all delays'''
    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    results = await asyncio.gather(*delays)
    return sorted(results)
