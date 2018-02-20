import numpy as np
import matplotlib.pyplot as plt

def plot_random_walk(num_steps):
    """
    Plots a random walk of length num_steps. The initial
    position is y = 0.
    
    Parameters
    ----------
    num_steps : int
        Number of steps to take in the random walk
    """
    y = np.zeros(num_steps)
    
    for i in range(1, num_steps):
        # YOUR CODE GOES HERE
        # 1. Generate an integer n which can be 0 or 1 (use the function numpy.random.randint)
        # 2. if n is 0, set y[i] to y[i-1]+1
        # 3. if n is 1, set y[i] to y[i-1]-1
        # -------------------
        
        
        
        # -------------------
        pass
    plt.plot(y)

number_of_walks = 10
number_of_steps = 100

for i in range(number_of_walks):
    plot_random_walk(number_of_steps)
