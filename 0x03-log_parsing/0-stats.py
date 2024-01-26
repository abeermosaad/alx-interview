#!/usr/bin/python3
""" Log parsing """
import re


def extract_input(input_line):
    """Extracts the relevant information from a line of input."""
    line = input_line.split(' ')
    return {
        'status_code': line[-2],
        'file_size': int(line[-1]),
    }


def print_stats(total_file_size, status_codes_stats):
    """Prints the accumulated statistics of the HTTP request log."""
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def run():
    """Starts the log parser."""
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            line_info = extract_input(line)
            code = line_info.get('status_code', '0')
            if code in status_codes_stats.keys():
                status_codes_stats[code] += 1
            total_file_size += line_info['file_size']
            line_num += 1
            if line_num % 10 == 0:
                print_stats(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError, SystemExit):
        print_stats(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
