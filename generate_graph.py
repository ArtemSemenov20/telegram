import numpy as np

def generate_data(num_points=100):
    X = np.linspace(0, 10, num_points)
    Y = 2 * X + 3 + np.random.normal(0, 1, num_points)
    return X, Y
