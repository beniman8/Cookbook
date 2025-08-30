import numpy as np
import matplotlib.pyplot as plt

# Define the number of coin flips (trials)
num_flips = 10000

# Simulate coin flips (0 for tails, 1 for heads)
# np.random.randint(0, 2, size=num_flips) generates random integers (0 or 1)
# for the specified number of flips.
coin_flips = np.random.randint(0, 2, size=num_flips)

# Calculate the cumulative mean of the coin flips
# np.cumsum(coin_flips) calculates the cumulative sum of heads
# np.arange(1, num_flips + 1) creates an array from 1 to num_flips, representing the number of trials
cumulative_mean = np.cumsum(coin_flips) / np.arange(1, num_flips + 1)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(cumulative_mean, label='Cumulative Mean of Flips')
plt.axhline(y=0.5, color='r', linestyle='--', label='Expected Mean (0.5)')
plt.xlabel('Number of Flips')
plt.ylabel('Proportion of Heads')
plt.title('Demonstration of the Law of Large Numbers (Coin Flips)')
plt.legend()
plt.grid(True)
plt.show()