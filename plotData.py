import matplotlib.pyplot as plt


def plot_data(X, y):
    
    """
     Instructions : Plot the training data into a figure using the matplotlib.pyplot
                    using the either "plt.scatter" or "plt.plot" function. Set the axis labels using
                    "plt.xlabel" and "plt.ylabel". Assume the population and revenue data
                    have been passed in as the x and y.    
    Parameters
    ----------
    x : array_like 
        Data point values for x-axis.

    y : array_like
        Data point values for y-axis. 
	Note x and y should have the same size.
	
	Hint : for plt.scatter function you can use the 'marker' parameter in the "plt.scatter" function to change the marker type (e.g. "x", "o").
            Furthermore, you can change the color of markers with 'color' parameter and change the marker size using 's' parameter.
	"""
	
	# ===================== Your Code Here =====================
    #plt.figure(figsize=(10,6))
    plt.scatter(X, y, marker='x', color = 'red', s = 50)
    plt.grid(True);
    
    
    

   # ===========================================================

    #plt.show()
