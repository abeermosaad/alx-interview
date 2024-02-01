#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    binary_list = []
    for char in data:
        if char > 247:
            return False
        binary_list.append(format(char, '#010b')[-8:])
    # print(binary_list)

    length = len(binary_list)
    for idx in range(length):
        if binary_list[idx][:5] == '11110' and length >= idx + 4:
            if binary_list[idx + 1][:2] == '10' and \
                binary_list[idx + 2][:2] == '10' and \
                    binary_list[idx + 3][:2] == '10':
                idx += 4
            else:
                return False
        elif binary_list[idx][:4] == '1110' and length >= idx + 3:
            if binary_list[idx + 1][:2] == '10' and\
                  binary_list[idx + 2][:2] == '10':
                idx += 3
            else:
                return False
        elif binary_list[idx][:3] == '110' and length >= idx + 2:
            if binary_list[idx + 1][:2] == '10':
                idx += 2
            else:
                return False
        elif binary_list[idx][:2] == '10' or binary_list[idx][:1] == '0':
            idx += 1
        else:
            return False
    return True
