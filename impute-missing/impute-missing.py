import numpy as np

def impute_missing(X, strategy='mean'):
    x = np.array(X, dtype=float)

    # Handle 1D case
    if x.ndim == 1:
        if strategy == "mean":
            value = np.nanmean(x)
        elif strategy == "median":
            value = np.nanmedian(x)
        else:
            raise ValueError("Invalid strategy")

        if np.isnan(value):
            value = 0.0

        x[np.isnan(x)] = value
        return x

    # 2D case
    if strategy == "mean":
        values = np.nanmean(x, axis=0)
    elif strategy == "median":
        values = np.nanmedian(x, axis=0)
    else:
        raise ValueError("Invalid strategy")

    # Replace NaN column values (all-NaN columns → 0)
    values = np.where(np.isnan(values), 0.0, values)

    inds = np.where(np.isnan(x))
    x[inds] = values[inds[1]]

    return x