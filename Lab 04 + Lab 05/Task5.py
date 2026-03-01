#Task 5
from queue import PriorityQueue
class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.g = 0  
        self.h = 0  
        self.f = 0 

    def __lt__(self, other):
        return self.f < other.f

class Environment:
    def __init__(self, graph, goals):
        self.graph = graph
        self.goals = goals

    def get_percept(self, start):
        return start

class GoalBasedAgent:
    def __init__(self, environment):
        self.environment = environment

    def best_first_search(self, start, goal):
        graph = self.environment.graph
        frontier = PriorityQueue()
        start_node = Node(start)
        frontier.put(start_node)
        visited = set()
        while not frontier.empty():
            current_node = frontier.get()
            current_state = current_node.state
            print("Visiting:", current_state)
            if current_state == goal:
                path = []
                while current_node:
                    path.append(current_node.state)
                    current_node = current_node.parent
                return path[::-1]
            visited.add(current_state)
            for neighbor, cost in graph[current_state]:
                if neighbor not in visited:
                    new_node = Node(neighbor, current_node)
                    new_node.g = current_node.g + cost
                    new_node.h = cost       
                    new_node.f = new_node.h
                    frontier.put(new_node)
        return None

    def multi_goal_search(self, start):
        current = start
        goals = self.environment.goals.copy()
        full_path = []
        print("Starting Multi-Goal Best-First Search...\n")
        while goals:
            nearest_goal = None
            shortest_estimate = float('inf')
            for g in goals:
                path = self.best_first_search(current, g)
                if path and len(path) < shortest_estimate:
                    shortest_estimate = len(path)
                    nearest_goal = g
            if not nearest_goal:
                print("No reachable remaining goal.")
                return None
            print("\nMoving to Goal:", nearest_goal)
            path = self.best_first_search(current, nearest_goal)
            if full_path:
                full_path.extend(path[1:])
            else:
                full_path.extend(path)
            current = nearest_goal
            goals.remove(nearest_goal)
            print("Remaining Goals:", goals)
            print("----------------------------------")
        return full_path

    def act(self, start):
        final_path = self.multi_goal_search(start)
        if final_path:
            print("\n✅ All Goals Visited!")
            print("Final Path:", " → ".join(final_path))
        else:
            print("❌ Could not visit all goals.")

graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [], 'E': [], 'F': [], 'G': [],
    'J': [], 'K': [], 'L': [], 'M': []
}
start_node = 'S'
goal_nodes = ['J', 'K', 'L', 'M']
environment = Environment(graph, goal_nodes)
agent = GoalBasedAgent(environment)
percept = environment.get_percept(start_node)
agent.act(percept)
