#!/usr/bin/python2
import sys
import numpy as np
import copy

class PriorityQueue:
    def __init__(self):
        self.list = []

    def add(self, state):
        self.list.append(state)

    def addFront(self, state):
        for i in reversed(state):
            self.list = [i] + self.list

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
   def sort_by_cost(self):#sort by the cost
        self.list.sort(key=itemgetter(3))


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
    print(np.matrix(temp_li))
    """
    temp_file = open('solution.txt','w')
    for item in temp_li:
        print>>temp_file, item
    """


def generateChild(parentNode, conditions):
    childx = []
    for i in range(0,6):
        childx.append((parentNode[0][i]+conditions[0][i]))
    child = [childx, conditions[1], conditions[2]]
    return child

def doAction(act, parentNode, childIndex):
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

def BFS(state, goal):
    node = state
    counter = 1
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
            # print "node not visited"
            # print node[0]
            # print " "
            explored.append(node[0])
            nodesVisited+=1

            #generate childs
            for i in range(0,5):
                child = doAction(i, node, counter)
                if child is not False:
                    if child[0] not in explored and not fronteir.found(child):
                        counter+=1
                        tree.append(child)
                        if np.array_equal(child[0],goal):
                            print "solution found"
                            print nodesVisited
                            # print child
                            solutionSet(tree, child)
                            return
                        fronteir.add(child)
                    # else:
                    #     print "ignore child"
    return

def DFS (state, goal):
    node = state
    counter = 1
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
            # print "node not visited"
            # print node
            # print " "
            explored.append(node[0])
            nodesVisited+=1

            childList = []
            #generate childs
            for i in range(0,5):
                child = doAction(i, node, counter)
                if child is not False:
                    if child[0] not in explored and not fronteir.found(child):
                        counter+=1
                        tree.append(child)
                        if np.array_equal(child[0],goal):
                            print "solution found"
                            print nodesVisited
                            # print child
                            solutionSet(tree, child)
                            return
                        childList += [child]
                    # else:
                    #     print "ignore child"
            fronteir.addFront(childList)
    return

def IDDFS (state, goal):
    step = 1
    while True:
        node = state
        depth = 0
        counter = 1
        nodesVisited = 0
        maxDepth = step
        print maxDepth
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
        nodeLevel = [1,0]

        while loopCounter:
            # exhausted search
            if fronteir.empty():
                #failed
                print "search failed"
                return

            #next node to visit
            node = fronteir.pop()

            #remove from level
            nodeLevel[0] -=1
            if nodeLevel[0] == 0:
                depth+=1

            #if node not yet visited
            if node[0] not in explored:
                # print "node not visited"
                # print node[0]
                # print " "
                explored.append(node[0])
                nodesVisited+=1

                count = 0
                #generate childs
                for i in range(0,5):
                    child = doAction(i, node, counter)
                    if child is not False:
                        if child[0] not in explored and not fronteir.found(child):
                            counter+=1
                            tree.append(child)
                            if np.array_equal(child[0],goal):
                                solutionSet(tree, child)
                                return
                            fronteir.add(child)
                            count +=1
                nodeLevel[1]+=count

            if nodeLevel[0] == 0:
                nodeLevel[0] = nodeLevel[1]
                nodeLevel[1] = 0

            if depth == maxDepth:
                loopCounter = False
                step+=1
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
        print(curr_node[0])

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

    DFS([0,0,0,3,3,1],[3,3,1,0,0,0])



if __name__ == "__main__":
    main()
