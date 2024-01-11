#!/usr/bin/python3
"""check if all boxes can be opened"""


def canUnlockAll(boxes):
    """check if all boxes can be opened"""
    keys = []
    keys.append(0)
    for box in range(len(boxes)):
        for key in boxes[box]:
            if key not in keys:
                if key != box and key < len(boxes):
                    keys.append(key)
    if len(keys) == len(boxes):
        return True
    return False
