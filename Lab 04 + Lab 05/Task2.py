def dls(graph, start, goal, depth_limit):
    visited = []
    def dfs(node, depth):
        if depth > depth_limit:
            return None  
        visited.append(node)
        print(f"Visiting: {node}, Depth: {depth}")
        if node == goal:
            print(f"\nGoal found with DLS. Path: {visited}")
            return visited.copy()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                path = dfs(neighbor, depth + 1)
                if path:
                    return path
        visited.pop()  
        return None
    result = dfs(start, 0)
    if result is None:
        return "Goal not found in this depth"
    return result

graph = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': ['G'],
'E': [],
'F': ['H'],
'G': [],
'H': []
}
print("Running DLS with Depth Limit = 2\n")
result1 = dls(graph, 'A', 'H', 2)
print("\nResult:", result1)

print("\nRunning DLS with Depth Limit = 3\n")
result2 = dls(graph, 'A', 'H', 3)
print("\nResult:", result2)
