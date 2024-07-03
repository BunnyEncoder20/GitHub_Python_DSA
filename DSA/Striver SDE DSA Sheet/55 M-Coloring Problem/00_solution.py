def graphColoring(graph,m,N):
    colors = [0]*N
    if solve(0,colors,m,N,graph):
        return True
    else:
        return False

def solve(node,colors,m,N,graph):
    # base case 
    if node==N : return True

    # remaining cases 
    for i in range(1,m+1):
        if isSafe(node,colors,N,i,graph):
            colors[node]=i
            if solve(node+1,colors,m,N,graph):
                return True
            colors[node]=0
    return False

def isSafe(node,colors,N,curr_color,graph):
    for k in range(N):
        if node!=k and graph[k][node]==1 and colors[k]==curr_color:
            return False
    return True
    
if __name__ == '__main__':
    N = 4
    m = 3
    graph = [[0 for i in range(N)] for j in range(N)]

    # Edges are (0, 1), (1, 2), (2, 3), (3, 0), (0, 2)
    graph[0][1] = 1
    graph[1][0] = 1
    graph[1][2] = 1
    graph[2][1] = 1
    graph[2][3] = 1
    graph[3][2] = 1
    graph[3][0] = 1
    graph[0][3] = 1
    graph[0][2] = 1
    graph[2][0] = 1

    print(1 if graphColoring(graph, m, N) else 0)