def value_grid_allocator(feature, dim):
    import numpy as np
    value_across_grid = []
    for item in feature:
        value_across_grid += int(item[0]) * [item[1]]
    value_across_grid=np.reshape(value_across_grid,(dim,1)).astype('float32')
    return value_across_grid

