#!/usr/bin/python2
import sys
import numpy as np

def main():
    for args in sys.argv[1:]:
        print args

    initial_state = sys.argv[1]
    goal_state = sys.argv[2]
    mode = sys.argv[3]
    output = sys.argv[4]

if __name__ == "__main__":
    main()