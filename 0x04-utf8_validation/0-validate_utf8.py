#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    num_bytes_to_follow = 0
    for char in data:
        binary = format(char, '#010b')[-8:]
        if num_bytes_to_follow == 0:
            if binary.startswith('0'):
                continue
            elif binary.startswith('110'):
                num_bytes_to_follow = 1
            elif binary.startswith('1110'):
                num_bytes_to_follow = 2
            elif binary.startswith('11110'):
                num_bytes_to_follow = 3
            else:
                return False
        else:
            if not binary.startswith('10'):
                return False
            num_bytes_to_follow -= 1
    return num_bytes_to_follow == 0
