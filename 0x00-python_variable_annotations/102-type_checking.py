#!/usr/bin/env python3
from typing import List, Tuple, Union

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """Returns a zoomed-in list by repeating each element in the tuple by the factor."""
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)  # Changed to a tuple to match the expected input type

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Corrected the factor to an integer

