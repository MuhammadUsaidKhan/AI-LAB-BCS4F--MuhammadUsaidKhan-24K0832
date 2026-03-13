#Task 2
class BeamEnvironment:
    def __init__(self, goal=20):
        self.goal = goal

    def heuristic(self, n):
        return abs(self.goal - n)

    def generate(self, x):
        return [x+2, x+3, x*2]


class BeamAgent:
    def __init__(self, env, beam_width=2):
        self.env = env
        self.k = beam_width

    def search(self, start):
        beam = [(start, [start])]
        level = 0
        while beam:
            print(f"\nLevel {level}: {[state for state, path in beam]}")
            candidates = []
            for state, path in beam:
                for new_state in self.env.generate(state):
                    new_path = path + [new_state]
                    if new_state == self.env.goal:
                        print("\nGoal reached!")
                        print("Path:", new_path)
                        return
                    candidates.append((new_state, new_path))
            candidates.sort(key=lambda x: self.env.heuristic(x[0]))
            beam = candidates[:self.k]
            level += 1

env = BeamEnvironment()
agent = BeamAgent(env, 2)
agent.search(1)
