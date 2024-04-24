graph = {
    'A': ['B','C'],
    'B': ['D', 'E'],
    'C': ['K'],
    'D': [],
    'E': ['K'],
    'K': []
}


def bfs(graph, node):
    queue = []
    visited = []
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0)    
        
        for val in graph[s]:
            if val not in visited:
                visited.append(val)
                queue.append(val)
            print(queue)
    return visited
        
print(bfs(graph, 'A'))