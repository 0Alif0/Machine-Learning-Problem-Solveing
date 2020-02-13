import numpy as np

def compute_cost(X, y, theta):
    # Initialize some useful values
    m = y.size
    cost = 0

    # ===================== Your Code Here =====================
    # Instructions : Compute the cost of a particular choice of theta.
    #                You should set the variable "cost" to the correct value.
    
    #theta_start is an n- dimensional vector of initial theta guess
    #X is matrix with n- columns and m- rows
    #y is a matrix with m- rows and 1 column
    
    #note to self: *.shape is (rows, columns)
    h= np.dot(X,theta)
    cost = (1/2*m) * np.sum(np.power((h-y),2))

        
    # ==========================================================

    return cost
