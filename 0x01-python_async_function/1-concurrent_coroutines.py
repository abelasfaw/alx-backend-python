#!/usr/bin/env python3
'''concurrent coroutine execution'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' spawns wait_random n times with the specified max_delay,
    and returns list of all delays'''
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(tasks)]
