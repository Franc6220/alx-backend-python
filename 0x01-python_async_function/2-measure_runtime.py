#!/usr/bin/env python3
import asyncio
import time
from typing import Any
from 1_concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Measure the average time per call of wait_n.

    Args:
        n (int): Number of times wait_random is spawned.
        max_delay (int): Maximum delay for each wait_random coroutine.

    Returns:
        float: Average time per call in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n

