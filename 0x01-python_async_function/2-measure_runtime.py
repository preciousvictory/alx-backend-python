#!/usr/bin/env python3
'''2-measure_runtime
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measure_time measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n
