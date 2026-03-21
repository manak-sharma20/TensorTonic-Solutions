import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X=np.array(X)
    nu=np.mean(X,axis=0)
    Xc=X-nu
    if X.ndim != 2:
        return None
    m,n=X.shape
    if m<2:
        return None
    return (1/(m-1))*Xc.T@Xc
    pass