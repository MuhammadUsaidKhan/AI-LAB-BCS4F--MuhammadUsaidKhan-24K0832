import random

class LearningBasedAgent:
    def __init__(self):
        self.Q = {'Play': 0, 'Rest': 0}
        self.alpha = 0.1
        self.actions_rewards = {'Play': 5, 'Rest': 1}

    def update_Q(self, action):
        self.Q[action] += self.alpha * (self.actions_rewards[action] - self.Q[action])

    def run(self, steps=10):
        for i in range(steps):
            action = random.choice(list(self.actions_rewards.keys()))
            reward = self.actions_rewards[action]
            self.update_Q(action)
            print(f"Step {i + 1}")
            print(f"Action {action} Reward +{reward}\n")

        print(f"\nQ-Table updated")
        print(self.Q)

agent = LearningBasedAgent()
agent.run()
