import random
class Environment:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def change_edge(self):
        node = random.choice(list(self.graph.keys()))
        if self.graph[node]:
            neighbor = random.choice(list(self.graph[node].keys()))
            old = self.graph[node][neighbor]
            new = max(1, old + random.choice([-3,-2,2,3]))
            self.graph[node][neighbor] = new
            print(f"Edge Changed: {node}->{neighbor} {old}->{new}")

class AdaptiveAStarAgent:
    def __init__(self, env):
        self.env = env

    def a_star(self, start, goal):
        frontier = [(start, self.env.heuristic[start])]
        g_cost = {start: 0}
        came_from = {start: None}
        visited = set()
        while frontier:
            frontier.sort(key=lambda x: x[1])
            current, _ = frontier.pop(0)
            if current in visited:
                continue
            visited.add(current)
            print("Visiting:", current)
            if random.random() < 0.3:
                self.env.change_edge()
            if current == goal:
                path = []
                while current:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]
            for neighbor, cost in self.env.graph[current].items():
                new_g = g_cost[current] + cost
                f = new_g + self.env.heuristic[neighbor]
                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    came_from[neighbor] = current
                    frontier.append((neighbor, f))
        return None
