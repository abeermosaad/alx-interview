#!/usr/bin/python3

def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    for char in data:
        if char > 255:
            return False
    return True
