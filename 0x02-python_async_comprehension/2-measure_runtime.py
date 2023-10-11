#!/usr/bin/env python3
'''2-measure_runtime
'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure_runtime
    '''
    start_time = time.time()
    coros = [async_comprehension() for _ in range(4)]
    data = await asyncio.gather(*coros)

    return (time.time() - start_time)
