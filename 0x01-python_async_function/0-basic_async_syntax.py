#!/usr/bin/env python3
'''
Async in Python
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''asynchronous coroutine that waits for a random delay'''
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
