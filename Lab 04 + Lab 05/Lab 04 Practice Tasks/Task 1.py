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
