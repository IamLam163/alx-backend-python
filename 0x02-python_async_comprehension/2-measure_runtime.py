#!/usr/bin/env python3
'''
running parallel tasks with async comprehensions
'''
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''running parallel tasks with async comprehensions'''
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter() - start
    return end
'''
async def main():
    return await(measure_runtime())

print(asyncio.run(main()))
'''
