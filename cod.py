import numpy as np
import matplotlib.pyplot as plt

def roll_standard_d20():
    """Roll a standard d20 die."""
    return np.random.randint(1, 21)

def roll_modified_d20(standard_die_result):
    """Roll a modified d20 die where the probability of rolling a 20 is 1/X, and other numbers equally share the remaining probability."""
    if np.random.random() < 1 / standard_die_result:
        return 20
    else:
        return np.random.choice([i for i in range(1, 20) if i != 20])

def roll_with_advantage():
    """Roll both dice and return the higher of the two."""
    standard_die = roll_standard_d20()
    modified_die = roll_modified_d20(standard_die)
    return max(standard_die, modified_die)

def monte_carlo_simulation(n=100000):
    """Perform a Monte Carlo simulation to estimate the probability distribution of rolling with advantage."""
    results = [roll_with_advantage() for _ in range(n)]
    frequency = {i: results.count(i) for i in range(1, 21)}
    probabilities = {k: (v / n) * 100 for k, v in frequency.items()}
    return probabilities

# Run the simulation and plot the results
probabilities = monte_carlo_simulation()

# Print the sorted dictionary
sorted_probabilities = dict(sorted(probabilities.items()))
print(sorted_probabilities)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(sorted_probabilities.keys(), sorted_probabilities.values(), color='blue')
plt.xlabel('Outcome')
plt.ylabel('Probability (%)')
plt.title('Probability Distribution of Rolling with Advantage')
plt.xticks(range(1, 21))
plt.grid(axis='y')
plt.show()
