from collections import deque


def canUnlockAll(boxes):
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
