#!/usr/local/bin/python3

import sys

def read_file(inputfile):
    with open(inputfile) as f: 
        pixels = [int(char) for char in f.readline().rstrip()]
    return pixels

def find_layers(pixels,layer_w,layer_h):
    line = [pixels[i:i+layer_w] for i in range(0,len(pixels), layer_w)]
    layers = [line[i:i+layer_h] for i in range(0,len(line), layer_h)]
    return layers

def print_layers(layers):
    min_count = [151,0,0]
    for layer in layers:
        counts = [0,0,0]
        for line in layer:
            counts[0] += line.count(0)
            counts[1] += line.count(1)
            counts[2] += line.count(2)
        if(counts[0] < min_count[0]):
            min_count = counts.copy()
    print("Min Zeros:",min_count, min_count[1] * min_count[2])

def overlay_layers(layers):
    message = [[2 for i in range(len(layers[0][0]))] for j in range(len(layers[0]))]
    for layer in range(0,len(layers)):
        for line in range(0,len(layers[layer])):
            for pixel in range(0,len(layers[layer][line])):
                if(message[line][pixel] == 2 and layers[layer][line][pixel] == 1):
                    message[line][pixel] = '\033[47m '
                elif(message[line][pixel] == 2 and layers[layer][line][pixel] == 0):
                    message[line][pixel] = '\033[40m ' 

    for line in message:
        print("".join(line))


def main():
    if len(sys.argv) > 3:
        input_file = sys.argv[1]
        layer_w = int(sys.argv[2])
        layer_h = int(sys.argv[3])
    elif len(sys.argv) > 1: 
        input_file = sys.argv[1]
        layer_w = 3
        layer_h = 2
    else:
        input_file = 'inputtest.txt'
        layer_w = 3
        layer_h = 2

    pixels = read_file(input_file)
    layered = find_layers(pixels,layer_w,layer_h)
    print_layers(layered)
    overlay_layers(layered)

if __name__ == '__main__':
    main()
