#!/usr/local/bin/python3

import sys

def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'inputtest.txt'
if __name__ == '__main__':
    main()
