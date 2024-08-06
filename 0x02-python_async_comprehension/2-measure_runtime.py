#!/usr/bin/env python3
import asyncio
import time
from typing import List
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """Measure the total runtime of executing async_comprehension four times in parallel."""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.time() - start_time
    return total_time

