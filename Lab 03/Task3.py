class GoalBasedAgent:
    def __init__(self, subjects):
        self.subjects = subjects
        self.completed_subjects = []

    def action(self):
        for subject in self.subjects:
            if subject not in self.completed_subjects:
                print(f"Studying {subject} ")
                self.completed_subjects.append(subject)
                print(f"Study session for {subject} completed.\n")

        if len(self.completed_subjects) == len(self.subjects):
            print("Goal achieved: All subjects completed")

agent = GoalBasedAgent(["AI", "Maths", "Physics"])
agent.action()
