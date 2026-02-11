import random

class Environment:
    def __init__(self):
        self.student_present = random.choice(["Yes", "No"])
        self.light_status = "OFF"

    def get_percept(self):
        return {'student': self.student_present, 'light': self.light_status}
    
    def update_student_presence(self):
        self.student_present = random.choice(["Yes", "No"])

    def light_on(self):
        self.light_status = "ON"

    def light_off(self):
        self.light_status = "OFF"

     
class ModelBasedAgent:
    def __init__(self):
        self.model = {'prev_student': None, 'prev_light': None, 'curr_student': None, 'curr_light': None}

    def act(self, percept):
        self.model['prev_student'] = self.model['curr_student']
        self.model['prev_light'] = self.model['curr_light']
        self.model['curr_student'] = percept['student']
        self.model['curr_light'] = percept['light']

        if self.model['curr_student'] == "Yes" and self.model['curr_light'] == "OFF":
            return "Turn light ON"
        elif self.model['curr_student'] == "No" and self.model['curr_light'] == "ON":
            return "Turn light OFF"
        else:
            return "No action"


def run_program(agent, env, steps):
    for i in range(steps):
        print(f"\nStep {i + 1}:")

        env.update_student_presence()
        percept = env.get_percept()
        action = agent.act(percept)

        if action == "Turn light ON":
            env.light_on()
        elif action == "Turn light OFF":
            env.light_off()

        print(f"Percept: {percept}")
        print(f"Action: {action}")
        print(f"Agent Model: {agent.model}")


agent = ModelBasedAgent()
env = Environment()
run_program(agent, env, steps=8)
