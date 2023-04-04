#!/usr/bin/env python3
'''
refactoring wait_n
'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''function returns list of all delays'''
    delays = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))
    result = await asyncio.gather(*delays)
    return sorted(result)

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
