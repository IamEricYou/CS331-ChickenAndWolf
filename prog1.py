#!/usr/bin/python2
import sys
import numpy as np

def read_file(initial):
    with open(initial) as f:
        line = f.read().splitlines()

    #print(line)
    return line

def main():
    if len(sys.argv) != 5:
        print('Usage: < initial state file > < goal state file > < mode > < output file >')
        return None

    initial_state = read_file(sys.argv[1])
    goal_state = read_file(sys.argv[2])
    mode = sys.argv[3]
    output = sys.argv[4]

    

if __name__ == "__main__":
    main()