#!/usr/bin/python3


def canUnlockAll(boxes):
    """function determines if all the boxes can be opened."""
    n = len(boxes)
    visited = set()

    def dfs(box_index):
        if box_index in visited or box_index >= n or box_index < 0:
            return

        visited.add(box_index)

        for key in boxes[box_index]:
            dfs(key)

    dfs(0)
    """return len visited"""
    return len(visited) == n
