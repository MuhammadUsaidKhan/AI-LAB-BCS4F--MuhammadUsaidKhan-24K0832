from queue import PriorityQueue
class DeliveryEnvironment:
    def __init__(self, graph, time_windows):
        self.graph = graph
        self.time_windows = time_windows

class DeliveryAgent:
    def __init__(self, env):
        self.env = env

    def greedy_delivery(self, start):
        current = start
        visited = set([start])
        total_distance = 0
        route = [start]
        deliveries = list(self.env.time_windows.keys())
        while deliveries:
            pq = PriorityQueue()
            for city in deliveries:
                if city not in visited:
                    distance = self.env.graph[current][city]
                    deadline = self.env.time_windows[city]
                    priority = deadline + distance
                    pq.put((priority, city))
            if pq.empty():
                break
            _, next_city = pq.get()
            total_distance += self.env.graph[current][next_city]
            route.append(next_city)
            visited.add(next_city)
            deliveries.remove(next_city)
            current = next_city
        return route, total_distance

graph = {
    'S': {'A':4,'B':6,'C':8},
    'A': {'B':2,'C':5,'S':4},
    'B': {'A':2,'C':3,'S':6},
    'C': {'A':5,'B':3,'S':8}
}
time_windows = {
    'A': 5,
    'B': 2,
    'C': 8
}
env = DeliveryEnvironment(graph, time_windows)
agent = DeliveryAgent(env)
route, distance = agent.greedy_delivery('S')
print("Route:", route)
print("Total Distance:", distance)
