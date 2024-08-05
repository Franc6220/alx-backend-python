#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously wait for a random delay and return it.

    Args:
        max_delay (int): The maximum delay time in seconds (default is 10).

    Returns:
        float: The delay time in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

