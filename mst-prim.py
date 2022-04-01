# Nikhil Solanki
# CS 260
# HW 08 Part 1 ~ My lab group (Eric, Aidan and Manish) and I worked on this together

#THIS FILE IS FOR PRIM'S ALGORITHM ONLY ; mst-kruskal.py is for Kruskal's

import heapq
import math

# From HW 7
class AdjacencyMatrix: 
    #Initialize an empty matrix, filled with infinities

    def __init__(self, n): #Aidan helped with some of these functions
        # Prim's UNCOMMENT THIS
        self.matrix = []

        for i in range(0, n):
            temp = [math.inf]*n
            self.matrix.append(temp)

    def __str__(self): #Return format for the matrix
        return "{}".format(self.matrix)

    def adj(self,x): # Professor Boady helped me with this // Return list of adjacent nodes
        adjacent = []
        size = len(self.matrix)
        for i in range(0, size):
            if self.matrix[x][i] > 0 and self.matrix[x][i] < math.inf:
                adjacent.append(i)
        #matrix.adj(x)
        return adjacent

    def weight(self,f,t): #Return weight of edges
        return self.matrix[f][t]
    
    def addEdge(self,f, t, w): #Add edge to matrix
        self.matrix[f][t] = w 
    
    def getMatrix(self): # Helper to return matrix
        return self.matrix

    def findSet(self, U, n):
        for i in U:
            if i.intersection({n}) == {n}:
                return i
    
def buildMatrix(file):
    with open(file + '.txt', "r") as file:
        size = int(file.readline()[0]) #First line of .txt file is the number of nodes (size of matrix)
        matrix = AdjacencyMatrix(size)
        for line in file:
            values = line.split(" ")
            if len(values) > 1: #Check if array from split is more than 1 element (valid to add edge)
                matrix.addEdge(int(values[0]), int(values[1]), int(values[2]))
                matrix.addEdge(int(values[1]), int(values[0]), int(values[2]))

    return matrix


def prim(G, start_node):
    matrix = G.getMatrix()
    H = []
    # m = [math.inf] * matrix # Matrix with infinities
    m = []
    U = {start_node} # add start node to set
    cnt = 0

    # for i in range(0, len(matrix)):
    #     x = [math.inf]* len(matrix)
    #     m.append(x)

    # for i in range(0, len(matrix)): #For every same value, set to zero (diagonals = 0)
    #      m[i][i] = 0

    for i in G.adj(start_node): #Adding the weights to the heap
        heapq.heappush(H, (G.weight(start_node, i), start_node, i))

    
    while cnt < len(matrix) - 1: #Aidan helped me with this 
        w, u, v = heapq.heappop(H)
        if v not in U: # Checks if we're making a cycle
            print(u, v, w)
            U = U.union({v}) #Adds v to set 
            for i in G.adj(v):
                heapq.heappush(H, (G.weight(v, i), v, i))
            cnt += 1
            m.append((u, v))
    
    return m

        # if matrix[start_node][i] != float("inf") and matrix[start_node][i] != 0: #Check if the adjacent node exists
        #     edgeWeight = matrix[start_node][i] #Weight at given index
        #     fromNode = start_node
        #     toNode = i
        #     edge = (edgeWeight, fromNode, toNode) #edge + from + to
        #     # H.append(edge)
        #     heapq.heappush(edge)



if __name__ == '__main__': 
    flag = True
    # Menu
    print("""
    There are 3 commands to choose from:\n
    " prim x " - Runs Prim's starting at node X. X must be an integer
    " help "
    " exit "
                """)

    while(flag):
        command = input("Enter a command: ")
        if command == "exit":
            flag = False
            #Exits the function
        if command == "prim":
            z = input("Enter the name of file to read: \n")
            start_node = input("Enter index value: \n")
            print("Running Prim's...\n")
            matrix = buildMatrix(z)
            print(prim(matrix, int(start_node)))
            flag = False

        if command == "help":
            print("""
                There are 3 commands to choose from:\n
                " prim x " - Runs Prim's starting at node X. X must be an integer
                " help "
                " exit "
                """)