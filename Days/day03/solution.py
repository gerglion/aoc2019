#!/usr/local/bin/python3

import sys,copy

def intcode(intcode_i):
    i = 0
    while(intcode_i[i] != 99):
        if(intcode_i[i] == 1):
            intcode_i[intcode_i[i+3]] = intcode_i[intcode_i[i+1]] + intcode_i[intcode_i[i+2]]
            i += 4
        elif(intcode_i[i] == 2):
            intcode_i[intcode_i[i+3]] = intcode_i[intcode_i[i+1]] * intcode_i[intcode_i[i+2]]
            i += 4
        else:
            break
    return intcode_i

def getIntcode(input_file):
    with open(input_file) as f:
        intcode_s = f.readline()
    intcode_s.rsplit()
    intcode_i = [int(x) for x in intcode_s.split(",")]
    return intcode_i

def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'inputtest.txt'

    # Get IntCode
    intcode_gold = getIntcode(input_file)

    # Part 1
    intcode_i = copy.copy(intcode_gold)
    intcode_i[1] = 12
    intcode_i[2] = 2
    part1 = intcode(intcode_i)
    print("Part 1:")
    print(part1[0])

    # Part 2
    for i in range(99):
        for j in range(99):
            intcode_i = copy.copy(intcode_gold)
            intcode_i[1] = i
            intcode_i[2] = j
            part2 = intcode(intcode_i)
            if(part2[0] == 19690720):
                print("Part 2:")
                print("100 *",str(i),"+",str(j),"=",str(100*i+j))
                #print(part2)
                break

if __name__ == '__main__':
    main()
