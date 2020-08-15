def pore_volume_func(old_pv,cell_pressure,ROCK):
    ref_pressure=[item[0] for item in ROCK][0]
    rock_compressibility =  [item[1] for item in ROCK][0]
    adjuster_factor=rock_compressibility*(cell_pressure-ref_pressure)
    new_pv=old_pv*(1+adjuster_factor+(adjuster_factor**2)/2)
    return new_pv