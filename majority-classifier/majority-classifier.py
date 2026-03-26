import numpy as np
from collections import Counter

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    freq=Counter(y_train)
    
    major=freq.most_common(1)[0][0]
    return  np.full(len(X_test),major)
    
    pass