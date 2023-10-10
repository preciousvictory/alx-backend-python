#!/usr/bin/env python3
'''4-tasks'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''task_wait_n task_wait_random that takes an integer max_delay
    '''
    coros = [task_wait_random(max_delay) for i in range(n)]
    wait_list = await asyncio.gather(*coros)

    return sorted(wait_list)
