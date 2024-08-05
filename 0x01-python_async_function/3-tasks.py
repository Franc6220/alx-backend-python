#!/usr/bin/env python3
import asyncio
from 0_basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio Task for wait_random with given max_delay.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The asyncio Task object.
    """
    return asyncio.create_task(wait_random(max_delay))

