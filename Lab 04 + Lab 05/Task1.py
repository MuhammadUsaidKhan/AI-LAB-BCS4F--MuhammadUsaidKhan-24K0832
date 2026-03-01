def grid_to_graph(grid):
    rows = len(grid)
    cols = len(grid[0])
    graph = {}
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  
                graph[(r,c)] = []
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            graph[(r,c)].append((nr,nc))
    return graph

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def bfs_search(self, graph, start, goal):
        visited = []
        queue = []
        parent = {}  
        visited.append(start)
        queue.append(start)
        parent[start] = None
        print("Traversal Order:")
        while queue:
            node = queue.pop(0)
            print(f"Visiting: {node}")
            if node == goal:
                path = []
                while node is not None:
                    path.append(node)
                    node = parent[node]
                path.reverse()
                print("\nShortest Path:", path)
                return f"\nGoal {goal} found!"
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    parent[neighbour] = node
        return "Goal not found"
    def act(self, percept, graph):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal reached":
            return f"Goal {self.goal} found!"
        else:
            return self.bfs_search(graph, percept, self.goal)

class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def run_agent(self, agent, start_node):
        percept = self.get_percept(start_node)
        action = agent.act(percept, self.graph)
        print(action)


building = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]
graph = grid_to_graph(building)
start = (0,0)
goal = (3,3)
agent = GoalBasedAgent(goal)
environment = Environment(graph)
environment.run_agent(agent, start)
