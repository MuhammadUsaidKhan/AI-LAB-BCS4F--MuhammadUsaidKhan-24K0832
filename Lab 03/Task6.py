class Environment:
    def __init__(self):
        self.rooms = {"a": "safe", "b": "safe", "c": "fire", "d": "safe", "e": "fire", "f": "safe", "g": "safe", "h": "safe", "j": "fire"}
        self.path = ["a", "b", "c", "d", "e", "f", "g", "h", "j"]

    def get_percept(self, room):
        return self.rooms[room]
    
    def extinguish_fire(self, room):
        self.rooms[room] = "safe"

    def display_env(self):
        print("Current Environment State:")
        for i in range(0, 9):
            if self.rooms[self.path[i]] == "safe":
                print("(:", end=" ")
            else:
                print(";)", end=" ")

            if (i % 3) == 2:
                print()
        print()


class FireFighterRobot:
    def __init__(self):
        self.path = ["a", "b", "c", "d", "e", "f", "g", "h", "j"]

    def run(self, env):
        for room in self.path:
            print(f"Robot has moved to Room \'{room}\'.")
            percept = env.get_percept(room)
            if percept == "safe":
                print(f"Room \'{room}\' is safe (no fires).")
            else:
                print(f"Fire detected in Room \'{room}\'. Extinguishing the fire...")
                env.extinguish_fire(room)
                print(f"Room \'{room}\' is now safe. Moving on.")

            env.display_env()

env = Environment()
agent = FireFighterRobot()
agent.run(env)
