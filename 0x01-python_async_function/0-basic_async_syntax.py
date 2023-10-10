#!/usr/bin/env python3
'''0-basic_async_syntax
'''
from random import uniform
import asyncio


async def wait_random(max_delay = 10):
    '''wait_random
    '''
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
