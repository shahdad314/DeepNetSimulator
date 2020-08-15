def gas_pvt_interp(cell_pressure, table, feature):
    import numpy as np
    x = [item[0] for item in table]
    if feature == 'bg':
        y = [item[1] for item in table]
    elif feature == 'mu':
        y = [item[2] for item in table]

    interp_value = np.interp(cell_pressure, x, y)
    return interp_value


def water_pvt_interp(cell_pressure, table, feature):
    import numpy as np
    ref_pressure = [item[0] for item in table][0]
    bw = [item[1] for item in table][0]
    cw = [item[2] for item in table][0]
    mw = [item[3] for item in table][0]
    cvw = [item[4] for item in table][0]

    y_factor = (cw - cvw) * (cell_pressure - ref_pressure)
    x_factor = cw * (cell_pressure - ref_pressure)

    cellbw = bw / (1 + x_factor + (x_factor * x_factor) / 2)
    cellmw = bw * mw / (1 + y_factor + (y_factor * y_factor) / 2) / cellbw

    if feature == 'bw':
        return cellbw
    elif feature == 'mw':
        return cellmw