# Author: Morgan Lavenstein Bendall
# Objective: This calls the function of our model and runs at different ds and dt.

import numpy as np
from function_upwind import UPW_SPM
from convergence_ds import convergence_ds_plt
from function_conservation import conservation_plt

# initial conditions
Smax = 15
Tmax = 10

dt = 0.01
ds = np.zeros([5])
# ds[0] = 0.9 * dt
# ds[1] = 0.9 * dt / 2
# ds[2] = 0.9 * dt / 4

ds[4] = 0.15
ds[3] = 0.2
ds[2] = 0.3
ds[1] = 0.4
ds[0] = 0.5

# ds = 0.9 * dt
# Ntest =  range(len(ds))
# filename = 'ds_convergence'

# initalize arrays
Ntime = int(Tmax/dt) + 1
time = np.linspace(0,Tmax, Ntime)


for i in range(len(ds)):

    print('Entering loop ' + str(i))


    # initalize arrays
    Nsize = int(Smax/ds[i]) + 1
    size = np.linspace(0,Smax, Nsize) # analytical solutions exist starting at 0.7

    data = 0 
    data = np.zeros([Ntime,Nsize])

    data = UPW_SPM(size, time, ds[i], dt)

    np.savetxt('ds_convergence/upwind_num_'+ str(i) +'.txt', data)  # save data to file

    print('Loop ' + str(i) + ' Complete.') # Progress update, loop end.

    # Plot numerical total population and error with true solution
    # conservation_plt(data, size, time, ds[i])

convergence_ds_plt(Smax, time, ds)

    # beep = np.loadtxt('ds_convergence/upwind_num_'+ str(i) +'.txt') # Load in relevant data.

    # print(np.shape(beep))

#   convergence_ds(size, time, ds, dt, Ntest, filename, data)
