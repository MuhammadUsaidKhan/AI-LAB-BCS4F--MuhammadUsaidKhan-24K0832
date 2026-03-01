class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, start):
        return start

class GoalBasedAgent:
    def __init__(self, goal, environment):
        self.goal = goal
        self.environment = environment

    def ucs(self, start):
        graph = self.environment.graph
        frontier = [(start, 0)] 
        visited = set()
        cost_so_far = {start: 0}
        came_from = {start: None}
        print("Starting Uniform Cost Search...\n")
        while frontier:
            frontier.sort(key=lambda x: x[1])
            current_node, current_cost = frontier.pop(0)
            print(f"Expanding Node: {current_node}, Cost so far: {current_cost}")
            if current_node in visited:
                continue
            visited.add(current_node)
            if current_node == self.goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                print("\n✅ Goal found with UCS.")
                print("Least Cost Path:", " → ".join(path))
                print("Total Cost:", current_cost)
                return
            for neighbor, cost in graph[current_node].items():
                new_cost = current_cost + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current_node
                    frontier.append((neighbor, new_cost))
        print("❌ Goal not found")

    def act(self, start_node):
        self.ucs(start_node)

graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'E': 3},
    'C': {'G': 4},
    'D': {'G': 1},
    'E': {'D': 4},
    'G': {}
}
start_node = 'S'
goal_node = 'G'
environment = Environment(graph)
agent = GoalBasedAgent(goal_node, environment)
percept = environment.get_percept(start_node)
agent.act(percept)
