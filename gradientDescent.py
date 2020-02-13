import numpy as np
from computeCost import *


def gradient_descent(X, y, theta, alpha, num_iters):
    # Initialize some useful values
    m = y.size
    J_history = np.zeros(num_iters)

    for i in range(0, num_iters):
        
        # Hint: X.shape = (97, 2), y.shape = (97, ), theta.shape = (2, )

        h=np.dot(X,theta)
        theta = theta - alpha *(1/m)* np.sum(np.power((h-y),2))
    
        # ===============================
        # Save the cost every iteration
        J_history[i] = compute_cost(X, y, theta)

    return theta, J_history
