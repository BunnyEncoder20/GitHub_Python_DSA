# M-Coloring Problem

Given an undirected graph and a number `m`, determine if the graph can be colored with at most `m` colors such that no two adjacent vertices of the graph are colored with the same color.

```
Example 1:
Input: 
N = 4
M = 3
E = 5
Edges[] = {
  (0, 1),
  (1, 2),
  (2, 3),
  (3, 0),
  (0, 2)
}
Output: 1
Explanation: It is possible to colour the given graph using 3 colours.

Example 2:
Input: 
N = 3
M = 2
E = 3
Edges[] = {
  (0, 1),
  (1, 2),
  (0, 2)
}

Output: 0
Explanation: It is not possible to color.
```

<br>

## The Only Approach 

### Algorithm

- [Watch it here](https://youtu.be/wuVwUK25Rfc?si=G6vnczG-379zdywb&t=258)
- For colors(1 to m): check if we can color that node with the selected color.
- If we can, we move to the next node and recursively keep going till we are at the last node
- If we cannot, then we take the next color
- If the recursion returns True, that sequence is valid
- If the recursion returns False, then that sequence is invalid. We need to backtrack and remove the previous colors we assigned.

### Code

```python
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

    # This is a adjacency matrix
    graph = [[0 for i in range(N)] for j in range(N)]

    # Edges are (0, 1), (1, 2), (2, 3), (3, 0), (0, 2)
    # Both ways cause it is a unidirectional graph
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
```
- Time complexity : O(N<sup>M</sup>)
  - We are checking all the M colors for N nodes
- Space complexity : O(N) + O(M)
  - O(N) for the auxiliary recursion space
  - O(M) for the color array