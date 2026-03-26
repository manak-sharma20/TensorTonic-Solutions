import numpy as np
from collections import Counter

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    classes= Counter(y)
    
    total=len(y)
    ent=0.0

    for x in classes.values():

        p=x/total
        if p>0:
            ent+=-p*np.log2(p)
    return ent
    

    
    