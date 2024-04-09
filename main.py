# Author: Morgan Lavenstein Bendall
# Objective: This calls the function of our model and runs at different ds and dt.

import numpy as np
from function_upwind import UPW_SPM
from convergence_ds import convergence_ds

# initial conditions
Smax = 15
Tmax = 2

dt = 0.01
# ds = np.zeros([1])
# ds[0] = 0.9 * dt
ds = 0.9 * dt
Ntest = 0
filename = 'test'

# initalize arrays
Nsize = int(Smax/ds) + 1
Ntime = int(Tmax/dt) + 1
size = np.linspace(0,Smax, Nsize)
time = np.linspace(0,Tmax, Ntime)

data = np.zeros([Ntime,Nsize])

with open(filename + 'up_' + str(Ntest) + '.txt', 'w') as file: # Initialise an outputter file (safe)

    data = UPW_SPM(size, time, ds, dt, Ntest, filename)

convergence_ds(size, time, ds, dt, Ntest, filename, data)



# filename = 'ds_convergence/' # Folder name for data storage.
# # filename = 'dt_convergence/' # Folder name for data storage.

# # Execute the model for each of the set of pairs of values ds/dt.
# for i,dsi in enumerate(dsvals):

#     print('Entering loop ' + str(i)) # Progress update, loop start.
#     # print("CFL " + str(dt) + "<" + str(np.exp(-0.4)*dsi)) # it seems to be meeing the CFL condition
#     # LW_SPM(dsi,dtvals[i],i,filename) # Model - ds run.
#     LW_SPM(dsi,dt,i,filename) # Model - dt run.
#     print('S Loop ' + str(i) + ' Complete.') # Progress update, loop end.