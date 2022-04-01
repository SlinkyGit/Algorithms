# Nikhil Solanki
# CS 260
# HW 08 Part 2 ~ My lab group (Eric, Aidan and Manish) and I worked on this together

#THIS FILE IS FOR KRUSKAL'S ALGORITHM ONLY ; mst-prim.py is for Prim's

import heapq
import math

# From HW 7
class AdjacencyMatrix: 
    #Initialize an empty matrix, filled with infinities

    def __init__(self, n): #Aidan helped with some of these functions
        self.matrix = {}
        for i in range(0, n):
            self.matrix[i] = {}

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

def kruskal(G): # Aidan's function
    matrix = G.getMatrix()
    g = []
    T = []
    U = []
    cnt = 0

    for i in matrix: #Multidimensional array, so fill rows x columns 
        for j in matrix[i]:
            g.append((matrix[i][j], i, j))

    g.sort() #Sort the edges

    for i in matrix:
        U.append({i})

    while cnt < len(matrix) - 1:
        w, u, v, = g.pop(0) # Pop first elements of individual lists
        x = G.findSet(U, u)
        y = G.findSet(U, v)

        if x.intersection(y) != x:
            U.remove(x) #Remove the duplicates; already traversed
            U.remove(y)
            U.append(x.union(y))
            T.append((u, v, w))
            cnt+=1
        
    return T
        

if __name__ == '__main__': 
    flag = True
    # Menu
    print("""
    There are 3 commands to choose from:\n
    " kruskal " - Runs Kruskal's
    " help "
    " exit "
                """)

    while(flag):
        command = input("Enter a command: ")
        if command == "exit":
            flag = False
            #Exits the function
    
        if command == "kruskal":
            z = input("Enter the name of file to read: \n")
            print("Running Kruskal's...\n")
            matrix = buildMatrix(z)
            print(kruskal(matrix))
            flag = False

        if command == "help":
            print("""
                There are 3 commands to choose from:\n
                " kruskal " - Runs Kruskal's
                " help "
                " exit "
                """)