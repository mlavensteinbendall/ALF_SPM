import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

def convergence_ds(size, time, ds, dt, ntag,filename, data):

    # # initalize arrays
    # Nsize = int(Smax/ds) + 1
    # Ntime = int(Tmax/dt) + 1
    # size = np.linspace(0,Smax, Nsize)
    # time = np.linspace(0,Tmax, Ntime)

    Tend = time[-1]
    # print(Tend)

    # Analytical Solution
    Y   = np.log(np.exp(size) - Tend)
    phi = np.exp(-((Y-5)/1)**2) # Initial Conditions
    sol = phi * np.exp(Y - np.log(Tend + np.exp(Y)))  # g(s) = exp(-s), mu(s) = 0

    


    # Plot the Analytical and Numerical Solution
    plt.plot(size, sol, label='Analytical', linestyle='solid')
    plt.plot(size, data[0,:], label='Numerical', linestyle='--')
    # plt.axvline(x=0.4, color='r', linestyle='--', label='x=1')
    plt.xlabel('Size')
    plt.ylabel('Population')
    plt.title('Population Based on Size at time = 0')
    plt.legend()
    # plt.ylim(-.2, 1.4)  # Set y-axis limits from 0 to 12
    # plt.savefig('plots/pop_plot-time' + str(n) + '-ds_'+ str(ds_index) +'.png') # Save the plot
    plt.show()

    # Ntrue = 