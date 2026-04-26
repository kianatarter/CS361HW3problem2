'''
CS 361 HW 3
Kiana Tarter
Algorithm to check if a graph is a tree or not
Input: Adjacency list

'''

from collections import deque

def is_tree(graph, src):
    visited = set()
    q = deque([(src, None)])  

    while q:
        current, parent = q.popleft()

        if current in visited:
            return False  # cycle detected

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor != parent:
                q.append((neighbor, current))

    # check if connected
    if len(visited) != len(graph):
        return False

    return True
