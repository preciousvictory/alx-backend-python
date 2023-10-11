#!/usr/bin/env python3
'''0-async_generator
i'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''async_generator
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yeild random.random() * 10
