class Environment:
    def __init__(self, traffic_status = "Heavy Traffic"):
        self.traffic_status = traffic_status

    def get_percept(self):
        return self.traffic_status


class SimpleReflexAgent:
    def __init__(self):
        pass

    def act(self, percept):
        if percept == "Heavy Traffic":
            return "Extended Green Signal Time"
        else:
            return "Normal Green Signal Time"

      
def run_program(agent, env):
    percept = env.get_percept()
    action = agent.act(percept)
    print(f"Percept: {percept} ==> Action: {action}")


agent = SimpleReflexAgent()
env1 = Environment("Heavy Traffic")
env2 = Environment("Light Traffic")
run_program(agent, env1)
run_program(agent, env2)
