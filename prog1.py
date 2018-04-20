#!/usr/bin/python2
import sys
import numpy as np
import copy

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

    def found(self, search):
        for i in self.list:
            if search == i:
                return True
        return False

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

    print act
    if parentNode[0][5] == 1:
        if parentNode[0][3] > 0 and ((parentNode[0][3]-1) >= parentNode[0][4] or (parentNode[0][3]-1) ==0) and parentNode[0][0]+1 >= parentNode[0][1] and act == 0:
            return generateChild(parentNode, [[1,0,1,-1,0,-1], parentNode[2], childIndex])

        elif parentNode[0][3] > 1 and ((parentNode[0][3]-2) >= parentNode[0][4] or (parentNode[0][3]-2)==0) and parentNode[0][0]+2 >= parentNode[0][1] and act == 1:
            return generateChild(parentNode, [[2,0,1,-2,0,-1], parentNode[2], childIndex])

        elif (parentNode[0][4] > 0) and (parentNode[0][0] >= (parentNode[0][1]+1) or parentNode[0][0] == 0) and act == 2:
            return generateChild(parentNode, [[0,1,1,0,-1,-1], parentNode[2], childIndex])

        elif parentNode[0][4] > 0 and parentNode[0][3] > 0 and (parentNode[0][0] >= parentNode[0][1]) and act == 3:
            return generateChild(parentNode, [[1,1,1,-1,-1,-1], parentNode[2], childIndex])

        elif parentNode[0][4] > 1 and (parentNode[0][0] >= parentNode[0][1]+2 or parentNode[0][0] == 0) and act == 4:
            return generateChild(parentNode, [[0,2,1,0,-2,-1], parentNode[2], childIndex])

    elif parentNode[0][5] == 0:
        if parentNode[0][0] > 0 and ((parentNode[0][0]-1) >= parentNode[0][1] or (parentNode[0][0]-1) ==0) and (parentNode[0][3]+1) >= parentNode[0][4] and act == 0:
            return generateChild(parentNode, [[-1,0,-1,1,0,1], parentNode[2], childIndex])

        elif parentNode[0][0] > 1 and ((parentNode[0][0]-2) >= parentNode[0][1] or (parentNode[0][0]-2) ==0)and (parentNode[0][3]+2) >= parentNode[0][4] and act == 1:
            return generateChild(parentNode, [[-2,0,-1,2,0,1], parentNode[2], childIndex])

        elif parentNode[0][1] > 0 and (parentNode[0][3] >= (parentNode[0][4]+1) or parentNode[0][3] == 0) and act == 2:
            return generateChild(parentNode, [[0,-1,-1,0,1,1], parentNode[2], childIndex])

        elif parentNode[0][1] > 0 and parentNode[0][0] > 0 and (parentNode[0][3] >= parentNode[0][4]) and act == 3:
            return generateChild(parentNode, [[-1,-1,-1,1,1,1], parentNode[2], childIndex])

        elif parentNode[0][1] > 1 and (parentNode[0][3] >= (parentNode[0][4]+2) or parentNode[0][3] == 0) and act == 4:
            return generateChild(parentNode, [[0,-2,-1,0,2,1], parentNode[2], childIndex])
    return False

def solutionSet(tree, child):
    counter = 0
    temp = len(tree)-1
    list = []
    print(np.matrix(tree))
    list.append(tree[len(tree)-1][0])
    while True:
        if tree[len(tree)-counter-1][1] == -1:
            #list.append(tree[0][0])
            break;
        for num in range(0,temp):
            if tree[temp][1] == tree[num][2]:
                #print("Counter: " + str(temp) + "Num: " + str(num))
                list.append(tree[num][0])
                temp = num
                #print(temp)
                break;
            
        counter = counter + 1
    temp_li = []
    for i in reversed(list):
        temp_li.append(i)
    #print(np.matrix(temp_li))
    """
    temp_file = open('solution.txt','w')
    for item in temp_li:
        print>>temp_file, item
    """

def BFS(state, goal):
    node = state
    counter = 0
    nodesVisited = 0

    #initial node is the end goal
    if np.array_equal(node,goal):
        print counter
        print "solution found"
        return

    #set up queue, explored, and tree
    fronteir = PriorityQueue()
    fronteir.add([state,-1,0])
    explored = []
    tree = [[state,-1,0]]

    loopCounter = True
    while loopCounter:
        # exhausted search
        if fronteir.empty():
            #failed
            print "search failed"
            return

        #next node to visit
        node = fronteir.pop()

        #if node not yet visited
        if node[0] not in explored:
            print "node not visited"
            print node[0]
            print " "
            explored.append(node[0])
            nodesVisited+=1

            #generate childs
            for i in range(0,5):
                child = doAction(i, node, counter)
                if child is not False:
                    if child[0] not in explored and not fronteir.found(child):
                        counter+=1
                        if np.array_equal(child[0],goal):
                            print "solution found"
                            print nodesVisited
                            print child
                            solutionSet(tree, child)
                            return
                        fronteir.add(child)
                        tree.append(child)
                    else:
                        print "ignore child"
    return

def main():
    # for args in sys.argv[1:]:
    #     print args
    #
    # initial_state = sys.argv[1]
    # goal_state = sys.argv[2]
    # mode = sys.argv[3]
    # output = sys.argv[4]

    # node = [[2,2,1,1,1,0],-1,0]
    # counterx = 1
    # for i in range(0,5):
    #     child = doAction(i, node, counterx)
    #     if child is not False:
    #         counterx+=1

    BFS([0,0,0,3,3,1],[3,3,1,0,0,0])



if __name__ == "__main__":
    main()
