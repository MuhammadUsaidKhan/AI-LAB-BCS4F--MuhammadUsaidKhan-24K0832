#Task 4
import numpy as np
states = ["Sunny", "Cloudy", "Rainy"]
transition_matrix = np.array([
    [0.6, 0.3, 0.1],  
    [0.3, 0.4, 0.3],  
    [0.2, 0.3, 0.5]   
])
def simulate_weather(initial_state, days):
    current = initial_state
    sequence = [current]
    for _ in range(days):
        idx = states.index(current)
        next_state = np.random.choice(states, p=transition_matrix[idx])
        sequence.append(next_state)
        current = next_state
    return sequence
sequence = simulate_weather("Sunny", 10)
print("Weather:", " -> ".join(sequence))
rainy_days = sequence.count("Rainy")
def estimate_probability(trials=1000):
    count = 0
    for _ in range(trials):
        seq = simulate_weather("Sunny", 10)
        if seq.count("Rainy") >= 3:
            count += 1
    return count / trials
prob = estimate_probability()
print("Probability of >=3 rainy days:", prob)
