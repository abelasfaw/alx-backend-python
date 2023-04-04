#!/usr/bin/python3
'''parallel execution using gather'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''executes async_comprehension 4 times in parallel
    using asyncio.gather'''
    starting_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.time()
    return end_time - starting_time
