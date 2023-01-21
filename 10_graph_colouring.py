V = 4

def printConfiguration(colorArray):
    print("The assigned colors are as follows:")
    for i in range(4):
        print("Vertex: ", i, " Color: ", colorArray[i])

def isSafe(v, colorArray, vertex):
    for i in range(V):
        if graph[v][i] == 1 and colorArray[i] == vertex:
            return False
        return True

def graphColoringAlgorithmUtil(m, colorArray, currentVertex):
    if currentVertex == V:
        return True

    for i in range(1, m + 1):
        if isSafe(currentVertex, colorArray, i) == True:
            colorArray[currentVertex] = i
            if graphColoringAlgorithmUtil(m, colorArray, currentVertex + 1):
                return True

            colorArray[currentVertex] = 0


def graphColoringAlgorithm(colorArray, m):
    colorArray = [0] * V

    if graphColoringAlgorithmUtil(m, colorArray, 0) == None:
        print("Coloring is not possible!")
        return False

    print("Coloring is possible!")
    printConfiguration(colorArray)
    return True



graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 3

graphColoringAlgorithm(graph, m)