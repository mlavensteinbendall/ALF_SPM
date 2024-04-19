# Author: Morgan Lavenstein Bendall
# Objective: This calls the function of our model and runs at different ds and dt.

import numpy as np
from function_upwind_size        import UPW_SPM
from convergence_ds         import convergence_ds_plt
from function_conservation  import conservation_plt
from convergence_dt         import convergence_dt_plt

# initial conditions
Smax = 15
Tmax = 2

ntests = 5

dt = 0.01



# ds 
# ds = np.zeros([5])
# ds[4] = 0.15
# ds[3] = 0.2
# ds[2] = 0.3
# ds[1] = 0.4
# ds[0] = 0.5


# Spatial grid step
ds = np.zeros(ntests)
ds[0] = 0.0125; ds[1] = 0.025
ds[2] = 0.05; ds[3] = 0.10
ds[4] = 0.20

# Temporal grid step
# dt = np.zeros(ntests)
# dt[0] = 0.0125/2; dt[1] = 0.0250/2
# dt[2] = 0.05/2; dt[3] = 0.10/2
# dt[4] = 0.20/2

# ds = 0.9 * dt
# Ntest =  range(len(ds))
# filename = 'ds_convergence'



for i in range(len(ds)):

    print('Entering loop ' + str(i))

    print(ds[i])

    # initalize arrays
    Nsize = int(Smax/ds[i]) + 1
    size = np.linspace(0,Smax, Nsize) # analytical solutions exist starting at 0.7

    # initalize arrays
    Ntime = int(Tmax/dt[i]) + 1
    time = np.linspace(0,Tmax, Ntime)

    data = 0 
    data = np.zeros([Ntime,Nsize])

    data = UPW_SPM(size, time, ds[i], dt[i])

    np.savetxt('ds_convergence/upwind_num_'+ str(i) +'.txt', data)  # save data to file

    print('Loop ' + str(i) + ' Complete.') # Progress update, loop end.

    # Plot numerical total population and error with true solution
    # conservation_plt(data, size, time, ds[i])

# Nsize = int(Smax/ds[4]) + 1
# size = np.linspace(0,Smax, Nsize) # analytical solutions exist starting at 0.7

# data = np.loadtxt('ds_convergence/upwind_num_4.txt')

# conservation_plt(data, size, time, ds[4])
# convergence_ds_plt(Smax, time, ds)

convergence_dt_plt(Smax, Tmax, ds, dt)


    # beep = np.loadtxt('ds_convergence/upwind_num_'+ str(i) +'.txt') # Load in relevant data.

    # print(np.shape(beep))

#   convergence_ds(size, time, ds, dt, Ntest, filename, data)
