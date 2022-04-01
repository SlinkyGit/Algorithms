# Nikhil Solanki
# CS 260 ~ HW 07
# My lab-mates (Eric and Aidan) and I worked on this assignment together. We helped each other with some of the functions.
import heapq
import math

# Input1.txt:
# matrix = [
# #   [0    1    2    3    4] 
#     [0, 1, math.inf, 2, 5],
#     [math.inf, 0, 2, math.inf, math.inf],
#     [1, math.inf, 0, 2, 4],
#     [math.inf, 1, 3, 0, math.inf],
#     [math.inf, math.inf, math.inf, 5, 0],
#     ]

class AdjacencyMatrix: 
    #Initialize an empty matrix, filled with infinities
    def __init__(self, n): #Aidan helped with some of these functions
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
    

def buildMatrix(file): #Aidan helped me with this function
    with open(file + '.txt', "r") as file:
        size = int(file.readline()[0]) #First line of .txt file is the number of nodes (size of matrix)
        matrix = AdjacencyMatrix(size)
        for line in file:
            values = line.split(" ")
            if len(values) > 1: #Check if array from split is more than 1 element (valid to add edge)
                matrix.addEdge(int(values[0]), int(values[1]), int(values[2]))
    return matrix

# z = input("Enter the name of file to read: \n")
# matrix = buildMatrix(z)
#print(matrix.adj(x))


def dijkstra(G, start_node): #Aidan helped with the initialization and I implemented the pseudocode from Professor Boady
    matrix = G.getMatrix()
    #s = set(start_node)
    Q = []
    d = [math.inf]* len(matrix) #Creates empty distance matrix with infinities
    d[start_node] = 0
    for i in range(len(d)):
        heapq.heappush(Q, (d[i], i)) #Filling heap with infinities
    while len(Q) > 0:
        u = heapq.heappop(Q)[1] #Grab 2nd value of tuple ~ min
        #s = s.union(set(u)) #Put min in empty set
        a = G.adj(u)
        for v in a:
            if d[v] > d[u] + G.weight(u,v):
                d[v] = d[u] + G.weight(u,v)
                heapq.heappush(Q, (d[v], v))
    
    return d

#print(dijsktra(matrix, 4))

if __name__ == '__main__': 
    flag = True
    # Menu
    print("""
        There are 3 commands to choose from:\n
        " dijkstra x " - Runs Dijkstra starting at node X. X must be an integer
        " help "
        " exit "
                """)

    while(flag):
        command = input("Enter a command: ")
        if command == "exit":
            flag = False
            #Exits the function
        if command == "dijkstra":
            z = input("Enter the name of file to read: \n")
            start_node = input("Enter index value: \n")
            matrix = buildMatrix(z)
            print(dijkstra(matrix, int(start_node)))
            flag = False
        if command == "help":
            print("""
            There are 3 commands to choose from:\n
            " dijkstra x " - Runs Dijkstra ; You will be prompted for your file and then enter X (an integer)
            " help "
            " exit "
                """)