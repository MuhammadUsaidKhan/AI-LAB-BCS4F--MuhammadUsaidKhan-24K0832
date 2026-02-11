class UtilityBasedAgent:
    def __init__(self, restaurants):
        self.restaurants = restaurants

    def act(self):
        utilities = {}
        for rest_name, rest_values in self.restaurants.items():
            utilities[rest_name] = rest_values['Rating'] - rest_values['Distance']
            print(f"Restaurant {rest_name} Utility: {utilities[rest_name]}")

        # key = utilities.get ensures that the max() compares dictionary values, not keys
        best_restaurant = max(utilities, key = utilities.get)
        print(f"\nSelected Restaurant: {best_restaurant}")

agent = UtilityBasedAgent({'A': {"Distance": 3, "Rating": 7}, 'B': {"Distance": 5, "Rating": 9}})
agent.act()
