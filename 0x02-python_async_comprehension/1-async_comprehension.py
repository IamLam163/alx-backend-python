#!/usr/bin/env python3
'''
using async comprehension
'''
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''writing async comprehension'''
    return [randm async for randm in async_generator()]
