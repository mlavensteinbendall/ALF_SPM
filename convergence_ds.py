import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

def convergence_ds_plt(Smax, time, ds):

    Tend = time[-1]
    Ntest = len(ds)

    Norm2 = np.zeros([Ntest])
    NormMax = np.zeros([Ntest])

    L2norm = np.zeros([Ntest-1])
    LMaxnorm = np.zeros([Ntest-1])


    for i in range(0, Ntest):

        Nsize = int(Smax/ds[i])+1
        size = np.zeros([Nsize])
        size = np.linspace(0,Smax,Nsize) # Create an array of those sizes.

        data = np.loadtxt('ds_convergence/upwind_num_' + str(i) + '.txt') # Load in relevant data.

        # Analyticial solution -- changes for what ds is
        c = 1/10
        Y   = 1/c * np.log(np.exp(size*c) - Tend*c)                       # g(s) = exp(-s/10)
        phi = np.exp(-((Y - 5) / 1) ** 2)                                 # initial condition
        sol = phi * np.exp( c**2 * (Y -  np.log( c*Tend + np.exp(Y) ) ) ) # g(s) = exp(-s/10), mu(s) = 0


        # Solve for L-2 and L-max
        Norm2[i]    = ( ( 1 / len(size) ) * np.sum( ( data[-1,:] - sol[:] ) **2 ) ) **0.5 # L2 error.
        NormMax[i]  = np.max( np.abs( data[-1,:] - sol[:] ) )                             # L-Max error.

        if i > 0 :
            # Loop through the remaining datasets.
            for ii in range(1,Ntest):
                L2norm[ii-1]    = np.log( Norm2[ii-1]   / Norm2[ii] )   / np.log( ds[ii-1] / ds[ii] )
                LMaxnorm[ii-1]  = np.log( NormMax[ii-1] / NormMax[ii] ) / np.log( ds[ii-1] / ds[ii] )



    for i in range(0, Ntest):

        print('For ds ='    + str( round( ds[i],10      ) ) )
        print('Norm 2 : '   + str( round( Norm2[i], 10  ) ) )
        print('Norm inf : ' + str( round( NormMax[i], 10) ) )

        if i > 0:
            print('L2 q error: '     + str( round( L2norm[ii-1]   , 10    ))) # L2 q estimate.
            print('LMax q error: '   + str( round( LMaxnorm[ii-1] , 10    ))) # L-Max q estimate.
            print(' ')

    # Plot the log-log for the errors.
    plt.loglog(ds, Norm2, label='Norm2')
    plt.loglog(ds, NormMax, label='NormMax')
    plt.loglog(ds, ds**1, label='order-1')

    plt.xlabel('ds')
    plt.ylabel('Norm')
    plt.title('Convergence based on ds')
    plt.legend()
    plt.show()


    # # Plot the Analytical and Numerical Solution
    # plt.plot(size, sol, label='Analytical', linestyle='solid')
    # plt.plot(size, data[-1,:], label='Numerical', linestyle='--')
    # # plt.axvline(x=0.4, color='r', linestyle='--', label='x=1')
    # plt.xlabel('Size')
    # plt.ylabel('Population')
    # plt.title('Population Based on Size at time = 0')
    # plt.legend()
    # # plt.ylim(-.2, 1.4)  # Set y-axis limits from 0 to 12
    # # plt.savefig('plots/pop_plot-time' + str(n) + '-ds_'+ str(ds_index) +'.png') # Save the plot
    # plt.show()