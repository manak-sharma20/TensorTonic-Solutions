import numpy as np

def calculate_eigenvalues(matrix):
    try:
        mat = np.array(matrix, dtype=float)
        
    
        if mat.ndim != 2 or mat.shape[0] != mat.shape[1]:
            return None
    
        return np.linalg.eigvals(mat)
    except:
        return None