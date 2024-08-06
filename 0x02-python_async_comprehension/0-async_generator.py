#!/usr/bin/env python3
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Yield a random float between 0 and 10 after asynchronously waiting 1 second, 10 times."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

