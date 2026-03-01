from queue import PriorityQueue
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

class Environment:
    def __init__(self, maze, goals):
        self.maze = maze
        self.goals = goals

    def valid_moves(self, pos):
        rows, cols = len(self.maze), len(self.maze[0])
        moves = []
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = pos[0]+dx, pos[1]+dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if self.maze[nx][ny] == 0:
                    moves.append((nx, ny))
        return moves

class GoalBasedAgent:
    def __init__(self, env):
        self.env = env

    def heuristic(self, pos, goal):
        return abs(pos[0]-goal[0]) + abs(pos[1]-goal[1])

    def best_first(self, start, goal):
        frontier = PriorityQueue()
        start_node = Node(start)
        frontier.put(start_node)
        visited = set()
        while not frontier.empty():
            current = frontier.get()
            if current.position == goal:
                path = []
                while current:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]
            visited.add(current.position)
            for move in self.env.valid_moves(current.position):
                if move not in visited:
                    node = Node(move, current)
                    node.h = self.heuristic(move, goal)
                    node.f = node.h
                    frontier.put(node)
        return None

    def multi_goal_search(self, start):
        current = start
        goals = self.env.goals.copy()
        full_path = []
        while goals:
            nearest = min(goals, key=lambda g: self.heuristic(current,g))
            path = self.best_first(current, nearest)
            if full_path:
                full_path.extend(path[1:])
            else:
                full_path.extend(path)
            current = nearest
            goals.remove(nearest)
        return full_path
