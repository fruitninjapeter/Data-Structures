def isBipartite(V, adj):
    # vector to store colour of vertex assigning all to -1 i.e. uncoloured
    # colours are either 0 or 1 for understanding take 0 as red and 1 as blue
    col = [-1] * (V)
    q = []  # queue for BFS storing {vertex , colour}
    for i in range(V):  # loop incase graph is not connected
        if (col[i] == -1):  # if not coloured
            q.append([i, 0])    # colouring with 0 i.e. red
            col[i] = 0
            while len(q) != 0:
                p = q[0]
                q.pop(0)    # pop current queue
                v = p[0]    # current vertex
                c = p[1]    # colour of current vertex
                for j in adj[v]:    # traversing vertexes connected to current vertex
                    if col[j] == c:   # if already coloured with parent vertex color, bipartite graph isn't possible
                        return False
                    if col[j] == -1:  # if uncoloured, colouring with opposite color to that of parent
                        if c == 1:
                            col[j] = 0
                        else:
                            col[j] = 1
                        q.append([j, col[j]])
    return True  # if all vertexes are coloured such that no two connected vertex have same colours


V, E = 4, 8
adj = []    # adjacency list for storing graph
adj.append([1, 3])
adj.append([0, 2])
adj.append([1, 3])
adj.append([0, 2])

ans = isBipartite(V, adj)
if (ans):
    print("Yes")
else:
    print("No")