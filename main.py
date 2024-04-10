# Author: Morgan Lavenstein Bendall
# Objective: This calls the function of our model and runs at different ds and dt.

import numpy as np
from function_upwind import UPW_SPM
from convergence_ds import convergence_ds

# initial conditions
Smax = 15
Tmax = 2

dt = 0.01
# ds = np.zeros([2])
# ds[0] = 0.9 * dt
# ds[1] = 0.9 * dt / 2
ds = 0.9 * dt
# Ntest =  range(len(ds))
filename = 'test'

# initalize arrays
Nsize = int(Smax/ds) + 1
Ntime = int(Tmax/dt) + 1
size = np.linspace(0,Smax, Nsize) # analytical solutions exist starting at 0.7
time = np.linspace(0,Tmax, Ntime)

data = np.zeros([Ntime,Nsize])

data = UPW_SPM(size, time, ds, dt)



# for i in 1:

#     print('Entering loop ' + str(i))

#     data = UPW_SPM(size, time, ds, dt)

#     np.savetxt(filename + 'upwind_num_' + str(i) + '.txt', data)

#     print('S Loop ' + str(i) + ' Complete.')

    # with open(filename + 'upwind_num_' + str(i) + '.txt', 'w') as file: # Initialise an outputter file (safe)






# print(np.shape(data))
# convergence_ds(size, time, ds, dt, Ntest, filename, data)


# filename = 'ds_convergence/' # Folder name for data storage.
# # filename = 'dt_convergence/' # Folder name for data storage.

# # Execute the model for each of the set of pairs of values ds/dt.
# for i,dsi in enumerate(dsvals):

#     print('Entering loop ' + str(i)) # Progress update, loop start.
#     # print("CFL " + str(dt) + "<" + str(np.exp(-0.4)*dsi)) # it seems to be meeing the CFL condition
#     # LW_SPM(dsi,dtvals[i],i,filename) # Model - ds run.
#     LW_SPM(dsi,dt,i,filename) # Model - dt run.
#     print('S Loop ' + str(i) + ' Complete.') # Progress update, loop end.