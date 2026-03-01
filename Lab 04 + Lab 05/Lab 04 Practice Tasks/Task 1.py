class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_actions(self, node):
        return self.graph.get(node, [])

class GoalBasedAgent:
    def __init__(self, goal, depth_limit):
        self.goal = goal
        self.depth_limit = depth_limit
        self.path = []

    def dls(self, env, node, depth):
        print(f"Visiting: {node}, Depth: {depth}")
        if depth > self.depth_limit:
            return False
        self.path.append(node)
        if node == self.goal:
            return True
        for neighbor in env.get_actions(node):
            if self.dls(env, neighbor, depth + 1):
                return True
        self.path.pop()
        return False

    def act(self, env, start):
        print("\nRunning Depth-Limited Search...\n")
        if self.dls(env, start, 0):
            print("\n✅ Goal Found!")
            print("Path:", self.path)
        else:
            print("\n❌ Goal Not Found within depth limit.")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}
env = Environment(graph)
agent = GoalBasedAgent(goal='G', depth_limit=2)
agent.act(env, 'A')

class UtilityBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def ucs(self, graph, start):
        frontier = [(start, 0)]
        visited = set()
        cost_so_far = {start: 0}
        came_from = {start: None}
        print("\nRunning Uniform Cost Search...\n")
        while frontier:
            frontier.sort(key=lambda x: x[1])
            current, cost = frontier.pop(0)
            if current in visited:
                continue
            print(f"Expanding: {current}, Cost: {cost}")
            visited.add(current)
            if current == self.goal:
                path = []
                while current:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                print("\n✅ Goal Found!")
                print("Path:", path)
                print("Total Cost:", cost)
                return
            for neighbor, edge_cost in graph[current].items():
                new_cost = cost + edge_cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current
                    frontier.append((neighbor, new_cost))
        print("\n❌ Goal Not Found")

graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'G': 5},
    'B': {'G': 10},
    'G': {}
}
agent = UtilityBasedAgent(goal='G')
agent.ucs(graph, 'S')
