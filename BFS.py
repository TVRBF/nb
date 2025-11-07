from collections import deque

# --------- BFS using Adjacency List ---------
def bfs(adj_list, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbour in adj_list[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    print()


# --------- DFS using Adjacency Matrix ---------
def dfs_matrix(adj_matrix, start, visited=None):
    if visited is None:
        visited = set()
        print("DFS Traversal:", end=" ")

    visited.add(start)
    print(chr(start + 65), end=" ")   # convert 0->A, 1->B, etc.

    for i in range(len(adj_matrix[start])):
        if adj_matrix[start][i] == 1 and i not in visited:
            dfs_matrix(adj_matrix, i, visited)
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}
adj_matrix = [
    [0,1,1,0,0],  # A connected to B, C
    [1,0,0,1,0],  # B connected to A, D
    [1,0,0,0,1],  # C connected to A, E
    [0,1,0,0,0],  # D connected to B
    [0,0,1,0,0]   # E connected to C
]
# BFS from A
bfs(adj_list, 'A')

# DFS from A (index 0)
dfs_matrix(adj_matrix, 0)
