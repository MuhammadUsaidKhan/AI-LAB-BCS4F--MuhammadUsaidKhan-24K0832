#Task 6
import random
class Environment:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def change_edge_cost(self):
        from_node = random.choice(list(self.graph.keys()))
        if not self.graph[from_node]:
            return None
        to_node = random.choice(list(self.graph[from_node].keys()))
        old_cost = self.graph[from_node][to_node]
        change = random.choice([-3, -2, 2, 3, 4])
        new_cost = max(1, old_cost + change)
        self.graph[from_node][to_node] = new_cost
        print(f"\n⚡ Edge cost changed: {from_node} → {to_node} "
              f"{old_cost} → {new_cost}")
        return (from_node, to_node)

class GoalBasedAgent:
    def __init__(self, environment):
        self.env = environment
        self.frontier = []
        self.visited = set()
        self.g_costs = {}
        self.came_from = {}

    def a_star(self, start, goal):
        self.frontier = [(start, self.env.heuristic[start])]
        self.visited = set()
        self.g_costs = {start: 0}
        self.came_from = {start: None}
        print("\nFollowing is the A* Search:")
        while self.frontier:
            self.frontier.sort(key=lambda x: x[1])
            current_node, current_f = self.frontier.pop(0)
            if current_node in self.visited:
                continue
            print(current_node, end=" ")
            self.visited.add(current_node)
            if random.random() < 0.3:
                self.env.change_edge_cost()
            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = self.came_from[current_node]
                path.reverse()
                print(f"\n\n✅ Goal found with A*. Path: {path}")
                print("Total Cost:", self.g_costs[goal])
                return
            for neighbor, cost in self.env.graph[current_node].items():
                new_g_cost = self.g_costs[current_node] + cost
                f_cost = new_g_cost + self.env.heuristic[neighbor]
                if (neighbor not in self.g_costs or
                        new_g_cost < self.g_costs[neighbor]):
                    self.g_costs[neighbor] = new_g_cost
                    self.came_from[neighbor] = current_node
                    self.frontier.append((neighbor, f_cost))
        print("\n❌ Goal not found")

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}
heuristic = {
    'A': 14, 'B': 12, 'C': 11,
    'D': 6, 'E': 4, 'F': 11, 'G': 0
}
environment = Environment(graph, heuristic)
agent = GoalBasedAgent(environment)
agent.a_star('A', 'G')
