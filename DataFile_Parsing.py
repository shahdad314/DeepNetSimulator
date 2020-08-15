from ParsingAlgorithm import *
from ValueAllocator import *
import numpy as np
from TimeStepGen import *
file = 'TEST0.DATA'
time_step = parsing_func(file,'TSTEP', '*')
dim = parsing_func(file,'DIMENS', ' ')
for item in dim:
    DIMENS= int(item[0] * item[1] * item[2])

### dx,dy,dz must be an array with the size of dimens
DX = parsing_func(file,'DX', '*')
DY = parsing_func(file,'DY', '*')
DZ = parsing_func(file,'DZ', '*')

DX = value_grid_allocator(DX, DIMENS)
DY = value_grid_allocator(DY, DIMENS)
DZ = value_grid_allocator(DZ, DIMENS)
PORO = parsing_func(file,'PORO', '*')
PORO = value_grid_allocator(PORO, DIMENS)

pv=np.multiply(PORO,(DIMENS))
pv.shape

PVT = parsing_func(file,'PVDG', ' ')
ROCK = parsing_func(x1,'ROCK', ' ')


DENSITY = parsing_func(x1,'DENSITY', ' ')[0]
Wloc1 = parsing_func2(x1,'WELSPECS', ' ', True)
Wloc2 = parsing_func2(x1,'COMPDAT', ' ', True)
parsing_func2(x1,'WCONPROD', ' ', True)


#same for permx, permy, permz