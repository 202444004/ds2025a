graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],   #A
    [1, 0, 0, 1, 0, 0, 0, 0],   #B
    [1, 0, 0, 1, 0, 0, 0, 0],   #C
    [0, 1, 1, 0, 1, 1, 1, 0],   #D
    [0, 0, 0, 1, 0, 1, 0, 0],   #E
    [0, 0, 0, 1, 1, 0, 0, 0],   #F
    [0, 0, 0, 1, 0, 0, 0, 1],   #G
    [0, 0, 0, 0, 0, 0, 1, 0]    #H
   # A  B  C  D  E  F  G  H
    #D-B-A-C-E-F-G-H
    #C-A-B-D-E-F-G-H
]

def dfs(g, i, visited):
    visited[i] = True
    print(chr(ord('A')+i), end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]: #중요
            dfs(g, j, visited)


visited_dfs = [False for _ in range(len(graph))]
dfs(graph, 2, visited_dfs)

