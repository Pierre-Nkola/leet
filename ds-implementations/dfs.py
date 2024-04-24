graph = {
    'A': ['B','C'],
    'B': ['D', 'E'],
    'C': ['K'],
    'D': [],
    'E': ['K'],
    'K': []
}

def dfs(grap, node):
    visited = []
    queue = []
    
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop()
        
        for val in grap[s][::-1]:
            if val not in visited:
                visited.append(val)
                queue.append(val)
    return visited

print(dfs(graph, 'A'))