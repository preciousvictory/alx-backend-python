#!/usr/bin/env python3
'''1-concurrent_coroutines'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''spawn wait_random n times with the specified max_delay
    '''
    coros = [wait_random(max_delay) for i in range(n)]
    wait_list = await asyncio.gather(*coros)

    return sorted(wait_list)
