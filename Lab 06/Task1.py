#Task 1
import random

class Environment:
    def __init__(self, min_x=0, max_x=6):
        self.min_x = min_x
        self.max_x = max_x

    def f(self, x):
        return -x**2 + 6*x

    def get_neighbors(self, x):
        neighbors = []
        if x + 1 <= self.max_x:
            neighbors.append(x + 1)
        if x - 1 >= self.min_x:
            neighbors.append(x - 1)
        return neighbors


class HillClimbingAgent:
    def __init__(self, environment):
        self.env = environment

    def search(self):
        current = random.randint(self.env.min_x, self.env.max_x)
        print("Initial x:", current)
        print("Initial f(x):", self.env.f(current))
        print()
        while True:
            neighbors = self.env.get_neighbors(current)
            best_neighbor = current
            best_value = self.env.f(current)
            for n in neighbors:
                value = self.env.f(n)
                if value > best_value:
                    best_neighbor = n
                    best_value = value
            if best_neighbor == current:
                print("No better neighbor found.")
                print("\nFinal Optimal Solution:")
                print("x =", current)
                print("f(x) =", self.env.f(current))
                break
            current = best_neighbor
            print("Move to x =", current, "f(x) =", self.env.f(current))

env = Environment()
agent = HillClimbingAgent(env)
agent.search()
