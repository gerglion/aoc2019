#!/usr/local/bin/python3

import sys

def intcode(input_file):
    #todo

def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'inputtest.txt'
    final_intcode = intcode(input_file)
    print(final_intcode)
if __name__ == '__main__':
    main()
