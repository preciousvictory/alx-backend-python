#!/usr/bin/env python3
'''1-async_comprehension'''
import asyncio
from typing import Generator


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    '''async_comprehension
    '''
    return [i async for i in async_generator()]
