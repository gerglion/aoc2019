#!/usr/local/bin/python3

import sys

def calc_total_fuel(input_file, fuel_weight=False):
    total_fuel = 0
    with open(input_file) as f:
        masses = [int(x) for x in f]
    for mod in masses:
        fuel = calc_module_fuel(mod,fuel_weight)
        total_fuel = total_fuel + fuel
    return total_fuel


def calc_module_fuel(mass,fuel_weight=False):
    fuel = max((mass // 3) - 2,0)
    if fuel_weight and fuel > 0:
        fuel = fuel + calc_module_fuel(fuel,True)
    return fuel

def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'part1.txt'
    total_fuel_pt1 = calc_total_fuel(input_file)
    print("Total fuel 1:",str(total_fuel_pt1))

    total_fuel_pt2 = calc_total_fuel(input_file,True)
    print("Total fuel 2:",str(total_fuel_pt2))

if __name__ == '__main__':
    main()
