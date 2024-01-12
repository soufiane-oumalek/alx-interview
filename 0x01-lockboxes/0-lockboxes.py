#!/usr/bin/python3


def canUnlockAll(boxes):
    """function determines if all the boxes can be opened."""

    total_boxes = len(boxes)
    opened_boxes = {0}
    keys_to_check = set(boxes[0])

    while keys_to_check:
        current_key = keys_to_check.pop()
        if 0 < current_key < total_boxes and current_key not in opened_boxes:
            opened_boxes.add(current_key)
            keys_to_check.update(boxes[current_key])
    """ return opened_boxes"""
    return len(opened_boxes) == total_boxes

