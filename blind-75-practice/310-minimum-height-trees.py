from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n:int, edges: List[List[int]]) -> List[int]:
        if n ==1:
            return [0]
        
        # Initialize a graph and a degree list to store the degree of each node
        graph = defaultdict(list)
        degree = [0] * n
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            degree[node1] += 1
            degree[node2] += 1
        
        # initialize a queue with all leaf nodes (nodes with degree 1)
        leaves_queue = deque(i for i in range(n) if degree[i] == 1)
        min_height_trees = []
        
        #keep trimming leaves until the centers(s) is/are found
        
        while leaves_queue:
            min_height_trees.clear()
            for i in range(len(leaves_queue)):
                current_node = leaves_queue.popleft()
                min_height_trees.append(current_node)
                #update the degrees of the current node's neighbors
                for neighbor in graph[current_node]:
                    degree[neighbor] -= 1
                    #if neighbour has become a leaf add it to the queue for processing in the next round
                    if degree[neighbor] == 1:
                        leaves_queue.append(neighbor)
        return min_height_trees
    
    
sol = Solution()
print(sol.findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]))
        
            