#!/usr/bin/python2
import sys
import numpy as np
import copy
from operator import itemgetter

class PriorityQueue:
    def __init__(self):
        self.list = []

    def add(self, state):
        self.list.append(state)

    def pop(self):
        return self.list.pop(0)

    def size(self):
        return len(self.list)

    def empty(self):
        if len(self.list)==0:
            return True
        return False

    def pQueue(self):
        for i in self.list:
            print i
        return

    def Found(self, search):
        for i in self.list:
            if search == i:
                return True
        return False
   
    def sort_by_cost(self):#sort by the cost
        self.list.sort(key=itemgetter(3))


def generateChild(parentNode, conditions):
    childx = []
    print parentNode
    print conditions
    for i in range(0,6):
        childx.append((parentNode[0][i]+conditions[0][i]))
    child = [childx, conditions[1], conditions[2]]
    print child
    return child

def doAction(act, parentNode, childIndex):
<<<<<<< HEAD
    """
    Act == 1 -> 1 chicken
    Act == 2 -> 2 chickens
    Act == 3 -> 1 chicken and 1 wolf
    Act == 4 -> 1 wolf
    Act == 5 -> 2 wolves
    """
=======

    print act
>>>>>>> 42695f8e3f180e148b92ee28e676f11bccaee862
    if parentNode[0][5] == 1:
        if parentNode[0][3] > 0 and ((parentNode[0][3]-1) >= parentNode[0][4]) and act == 0:
            return generateChild(parentNode, [[1,0,1,-1,0,-1], parentNode[2], childIndex])

        elif parentNode[0][3] > 1 and (parentNode[0][3]-2) >= parentNode[0][4] and act == 1:
            return generateChild(parentNode, [[2,0,1,-2,0,-1], parentNode[2], childIndex])

        elif (parentNode[0][4] > 0) and (parentNode[0][0] >= (parentNode[0][1]+1) or parentNode[0][0] == 0) and act == 2:
            return generateChild(parentNode, [[0,1,1,0,-1,-1], parentNode[2], childIndex])

        elif parentNode[0][4] > 0 and parentNode[0][3] > 0 and act == 3:
            return generateChild(parentNode, [[1,1,1,-1,-1,-1], parentNode[2], childIndex])

        elif parentNode[0][4] > 1 and (parentNode[0][0] >= parentNode[0][1]+2 or parentNode[0][0] == 0) and act == 4:
            return generateChild(parentNode, [[0,2,1,0,-2,-1], parentNode[2], childIndex])

    elif parentNode[0][5] == 0:
        if parentNode[0][0] > 0 and (parentNode[0][0]-1) >= parentNode[0][1] and act == 0:
            return generateChild(parentNode, [[-1,0,-1,1,0,1], parentNode[2], childIndex])

        elif parentNode[0][0] > 1 and (parentNode[0][0]-2) >= parentNode[0][1] and act == 1:
            return generateChild(parentNode, [[-2,0,-1,2,0,1], parentNode[2], childIndex])

        elif parentNode[0][1] > 0 and (parentNode[0][3] >= (parentNode[0][4]+1) or parentNode[0][3] == 0) and act == 2:
            return generateChild(parentNode, [[0,-1,-1,0,1,1], parentNode[2], childIndex])

        elif parentNode[0][1] > 0 and parentNode[0][0] > 0 and act == 3:
            return generateChild(parentNode, [[-1,-1,-1,1,1,1], parentNode[2], childIndex])

        elif parentNode[0][1] > 1 and (parentNode[0][3] >= (parentNode[0][4]+2) or parentNode[0][3] == 0) and act == 4:
            return generateChild(parentNode, [[0,2,1,0,-2,-1], parentNode[2], childIndex])

    return False

def BFS(state, goal):
    node = state
    counter = 0
    nodesVisited = 0
    if np.array_equal(node,goal):
        print counter
        return

    fronteir = PriorityQueue()
    fronteir.add([state,-1,0])
    explored = {}
    tree = [state]

    loopCounter = True
    while loopCounter:
        if fronteir.empty():
            #failed
            return

        #next node to visit
        node = fronteir.pop()

        #if node not yet visited
        if node[0] not in explored:
            explored.add(node[0])
            nodesVisited+=1

            #generate childs
            for i in range(0,4):
                child = doAction(i, node, counter)




                if child not in explored and not fronteir.found(child):
                    if np.array_equal(child,goal):
                        print counter
                        return
                    fronteir.add(child)
    return

def heristic_value(curr_node,goal_node):
    #print(curr_node[0])
    h_value  = (goal_node[0] - curr_node[0])+(goal_node[1] - curr_node[1]) 
    return h_value

def astar(initial,goal):
    #Pseudo Code for general a-star algorithm
    #while priority Queue Size
    #   current node = pq.pop
    #   if node == goal
    #       break
    #   for next node
    #       pq.push(next node, cost(node) + cost + heuristic(next node))
    counter = 0
    nodeVisited = 0
    frontier = PriorityQueue()
    frontier.add([initial,-1,0,heristic_value(initial,goal)])
    explored = []

    while True:
        if frontier.empty():
            print("No solutions found.")
            sys.exit(1)

        curr_node = frontier.pop()

        if np.array_equal(curr_node[0],goal):
            print("You found the solution")
            print("It took " + str(counter) + "steps")
            print(str(len(explored)) + "nodes were visited")
            break;
        #print(curr_node[:-1]) #remove last element
        print(curr_node)

        if curr_node[0] not in explored:
            explored.append(curr_node)
            #print(explored)
        frontier.sort_by_cost()
        

        #add node into explored
        #if child is not in explored
        #frontier.add(child)
        break;


def read_file(initial):
    with open(initial) as f:
        line1 = f.read().split('\n')[0].split(',')
    with open(initial) as f:
        line2 = f.read().split('\n')[1].split(',')

    return map(int,line1+line2) #convert list string to integer

def main():
    #if len(sys.argv) != 5:
    #    print('Usage: < initial state file > < goal state file > < mode > < output file >')
    #    sys.exit(1)

    node = [[2,2,1,1,1,0],-1,0]
    counterx = 1
    for i in range(0,5):
        child = doAction(i, node, counterx)
        if child is not False:
            counterx+=1
    #BFS([0,0,0,3,3,1],[3,3,1,0,0,0])
    """
    initial_state = read_file(sys.argv[1])
    goal_state = read_file(sys.argv[2])
    mode = sys.argv[3]
    output = sys.argv[4]
        
    if mode == "bfs":
        bfs(initial_state,goal_state)
    elif mode == "dfs":
        dfs(initial_state,goal_state)
    elif mode == "iddfs":
        iddfs(initial_state,goal_state)
    elif mode == "astar":
        astar(initial_state,goal_state)
    else:
        print("Wrong command. Check your command")
        return None
    """

if __name__ == "__main__":
    main()
