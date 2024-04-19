# Author: Morgan Lavenstein Bendall
# Objective: This calls the function of our model and runs at different ds and dt.

import numpy as np
from function_upwind_age    import UPW_SPM
# from convergence_ds         import convergence_ds_plt
from function_conservation  import conservation_plt
# from convergence_dt         import convergenc_dt_plt
from convergence_da         import convergence_da_plt
import matplotlib.pyplot as plt 

# initial conditions
Smax = 15
Tmax = 1
order = 2

ntests = 5

ds = np.zeros([ntests]) # order smallest to largest
# ds[4] = 0.1
# ds[3] = 0.2
# ds[2] = 0.3
# ds[1] = 0.4
# ds[0] = 0.5

# 1 order good
# ds[0] = 0.006
# ds[1] = 0.007 
# ds[2] = 0.008
# ds[3] = 0.009
# ds[4] = 0.01

# 2 order
ds[0] = 0.009**(1/2)
ds[1] = 0.01**(1/2)
ds[2] = 0.02**(1/2)
ds[3] = 0.03**(1/2)
ds[4] = 0.04**(1/2)


dt = 0.001

# initalize arrays
Ntime = int(Tmax/dt) + 1
time = np.linspace(0,Tmax, Ntime)

for i in range(len(ds)):

    print('Entering loop ' + str(i))

    print(ds[i])

    # initalize arrays
    Nsize = int(Smax/ds[i]) + 1
    size = np.linspace(0,Smax, Nsize) # analytical solutions exist starting at 0.7

    data = np.zeros([Ntime,Nsize])

    print('CFL: ' + str(round(dt/ds[i]**2, 2)))

    data = UPW_SPM(size, time, ds[i], dt, order)

    np.savetxt('ds_convergence/upwind_num_'+ str(i) +'.txt', data)  # save data to fileuu

    print('Loop ' + str(i) + ' Complete.') # Progress update, loop end.

    # conservation_plt(data, size, time, ds[i])

    # print(np.shape(data))


    # #analytical solution 
    # sol = np.zeros([len(time),len(size)])
    # c=1 # constant for mu
    # for i_t in range(0, len(time)):
    #     # Calculate the analytical solution
    #     sol[i_t,:] = np.exp(-(size - ( time[i_t] + 5))**2) * np.exp(- c * time[i_t]) #  mu(s) = 0


    # # Plots the numerical solution at multiple points in time
    # for t_index, n_t in enumerate(data):
    #     if t_index % 500 == 0:  # Plot only if time index is a multiple of 10
    #         plt.plot(size, data[t_index,:], label=f'Numerical at time {t_index }', linestyle='--')
    #         plt.plot(size, sol[t_index,:], label=f'Analytical at time {t_index }', linestyle='-')

    # plt.axhline(y=1, color='r', linestyle='--', label='y=1')
    # plt.xlabel('Age')
    # plt.ylabel('Population')
    # plt.title('Population by Age')
    # plt.legend()
    # plt.show()



convergence_da_plt(Smax, Tmax, ds, dt, order)