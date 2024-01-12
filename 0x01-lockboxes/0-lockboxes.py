#!/usr/bin/python3
"""import model"""
from collections import deque


def canUnlockAll(boxes):
    """function determines if all the boxes can be opened."""
    n = len(boxes)
    visited = set()
    queue = deque([0])

    while queue:
        current_box = queue.popleft()

        if current_box in visited:
            continue

        visited.add(current_box)
        queue.extend(boxes[current_box])

    return len(visited) == n
