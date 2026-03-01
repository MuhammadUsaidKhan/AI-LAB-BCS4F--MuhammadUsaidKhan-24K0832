class Environment:
    def __init__(self, tree):
        self.tree = tree

    def get_percept(self, start):
        return start

class GoalBasedAgent:
    def __init__(self, goal, environment):
        self.goal = goal
        self.environment = environment

    def dls(self, node, goal, depth, path):
        print(f"Visiting: {node}, Remaining Depth: {depth}")
        if depth == 0:
            return False
        if node == goal:
            path.append(node)
            return True
        if node not in self.environment.tree:
            return False
        for child in self.environment.tree[node]:
            if self.dls(child, goal, depth - 1, path):
                path.append(node)   
                return True
        return False

    def iterative_deepening(self, start, max_depth):
        for depth in range(max_depth + 1):
            print(f"Depth Level: {depth}")
            path = []
            if self.dls(start, self.goal, depth, path):
                print("\n✅ Goal Found!")
                print("Final Path:", " → ".join(reversed(path)))
                return
        print("\n❌ Goal not found within depth limit.")

    def act(self, start_node, max_depth):
        self.iterative_deepening(start_node, max_depth)

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}
start_node = 'A'
goal_node = 'G'
max_search_depth = 4
environment = Environment(tree)
agent = GoalBasedAgent(goal_node, environment)
percept = environment.get_percept(start_node)
agent.act(percept, max_search_depth) 
