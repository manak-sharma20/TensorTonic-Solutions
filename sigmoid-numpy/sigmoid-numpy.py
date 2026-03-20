import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    
    # Writer code here
    x=np.array(x)
    return 1/(1+np.exp(-x))
    
   