#!/usr/bin/env python3
import asyncio
from typing import List
from 0_basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with a max_delay, return the list of delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each wait_random coroutine.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    delays_list = await asyncio.gather(*delays)
    
    # Convert delays_list into a sorted list using an insertion sort method
    sorted_delays = []
    for delay in delays_list:
        inserted = False
        for i in range(len(sorted_delays)):
            if delay < sorted_delays[i]:
                sorted_delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            sorted_delays.append(delay)
    
    return sorted_delays

