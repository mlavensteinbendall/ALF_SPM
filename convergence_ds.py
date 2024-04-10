import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

def convergence_ds(size, time, ds, dt, ntag,filename, data):

    Tend = time[-1]

    # c = 1/10
    # Analytical Solution
    # Y   = 1/c * np.log(np.exp(size*c) - Tend*c)
    # phi = np.exp(-((Y-5)/1)**2) # Initial Conditions
    # sol = phi * np.exp(Y - np.log(Tend + np.exp(Y)))  # g(s) = exp(-s), mu(s) = 0

    c = 1/10
    Y = 1/c * np.log(np.exp(size*c) - Tend*c)  # g(s) = exp(-s/10)
    phi = np.exp(-((Y - 5) / 1) ** 2)
    # sol = phi * np.exp(c**2 * Y) * (c*Tend + np.exp(Y))**(-c**2)  # g(s) = exp(-s/10), mu(s) = 0
    sol = phi * np.exp( c**2 * (Y -  np.log( c*Tend + np.exp(Y) ) ) ) # g(s) = exp(-s/10), mu(s) = 0


    # Solve for L-2 and L-max
    Norm2 = ( ( 1 / len(size) ) * np.sum( ( data[-1,:] - sol[:] ) **2 ) ) **0.5 # L2 error.
    NormMax = np.max( np.abs( data[-1,:] - sol[:] ) ) # L-Max error.

    print('Norm 2 : ' + str(Norm2))
    print('Norm inf : ' + str(NormMax))


    # Plot the Analytical and Numerical Solution
    plt.plot(size, sol, label='Analytical', linestyle='solid')
    plt.plot(size, data[-1,:], label='Numerical', linestyle='--')
    # plt.axvline(x=0.4, color='r', linestyle='--', label='x=1')
    plt.xlabel('Size')
    plt.ylabel('Population')
    plt.title('Population Based on Size at time = 0')
    plt.legend()
    # plt.ylim(-.2, 1.4)  # Set y-axis limits from 0 to 12
    # plt.savefig('plots/pop_plot-time' + str(n) + '-ds_'+ str(ds_index) +'.png') # Save the plot
    plt.show()