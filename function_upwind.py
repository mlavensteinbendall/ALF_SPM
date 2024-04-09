# Current state
# d/dt(N) + d/ds (g(s)N) = mu N
# mu(s) = 0
# g(s) = exp(-s/10)


import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

def UPW_SPM(Smax, Tmax, ds, dt,ntag,filename):

    # initalize arrays
    Nsize = int(Smax/ds) + 1
    Ntime = int(Tmax/dt) + 1
    size = np.linspace(0,Smax, Nsize)
    time = np.linspace(0,Tmax, Ntime)

    # growth rate
    g = np.zeros([Nsize])
    g[:] = np.exp(-size[:]/10) 

    # mortality rate
    mu = np.zeros([Nsize])
    # mu = size

    # analytical derivative of growth rate !! ignore for right now !!
    gp = np.zeros([Nsize])
    gp[:] = - g[:]/10

    # inital condition -- population at t=0
    N = np.zeros([Ntime,Nsize])
    N[0,:] = np.exp(-(size[:]-5)**2)

    # with open(filename + 'up_' + str(ntag) + '.txt', 'w') as file: # Initialise an outputter file (safe)

    # print(np.size(N[0,0]))

    # for t in range(0, len(time) -1):

    #     for s in range(1,len(size)): 
            # print(s)
            # time splitting -- to solve numerically we are going to split this into 3 parts

            # # step 1 -- half time step
            # N[t+1,s] = - gp[s] * N[t,s] * 2/dt + N[t,s]

            # # step 2 -- time step 
            # N[t+1,s] = N[t,s] - dt * (g[s]*(N[t,s]-N[t,s-1])/ds + gp[s]* N[t,s])

            # # step 3 -- half time step
            # N[t+1,s] = - gp[s] * N[t,s] * 2/dt + N[t,s]


    # Here we have u_t + (gu)_s = 0
    # for t in range(0, len(time) -1):

    #     for s in range(1,len(size)): 
    #         Ntemp = 0

    #         Ntemp = N[t,s] - dt * (( g[s] * (N[t,s] - N[t,s-1])/ds ) + gp[s] * N[t,s] )
    #         # Ntemp = (1 - (dt/ds * g[s]) - dt * gp[s] ) * N[t,s] + ( g[s] * dt/ds * N[t,s-1]) 

    #         N[t+1,s] = Ntemp


    # for t in range(0, len(time) - 1):

    #     for s in range(1,len(size)): 
    #         N[t+1,s] = N[t,s] - dt * ( g[s] * (N[t,s] - N[t,s-1]) / ds + gp[s] * N[t,s])


    for t in range(0, len(time) -1):

        for s in range(1,len(size)): 
            Ntemp = 0

            # step 1 -- half time step
            Ntemp = N[t,s] * np.exp(mu[s] * dt/2)

            # step 2 -- time step 
            # Ntemp = Ntemp - dt * ((g[s]*(Ntemp - N[t,s-1])/ds) + gp[s]* Ntemp)
            # Ntemp = N[t,s] - dt * (( g[s] * (N[t,s] - N[t,s-1])/ds ) + gp[s] * N[t,s] )
            # Ntemp = (1 - (dt/ds * g[s]) - dt * gp[s] ) * N[t,s] + ( g[s] * dt/ds * N[t,s-1]) 

            Ntemp = N[t,s] - dt * ( g[s] * (N[t,s] - N[t,s-1])/ds )

            # step 3 -- half time step
            N[t+1,s] = Ntemp * np.exp(mu[s] * dt/2)
            # N[t+1,s] = Ntemp * np.exp(( -mu[s] - gp[s] ) * dt/2)


# on the board time splitting
    # for t in range(0, len(time) -1):

    #     for s in range(1,len(size)): 
    #         Ntemp = 0

    #         # step 1 -- half time step
    #         Ntemp = N[t,s] * np.exp( ( -mu[s] - gp[s] )* dt/2 )


    #         # step 2 -- time step 
    #         Ntemp = N[t,s] - dt * ( g[s] * (N[t,s] - N[t,s-1])/ds ) 

    #         # step 3 -- half time step
    #         N[t+1,s] = Ntemp * np.exp(( -mu[s] - gp[s] ) * dt/2)

# time splitting with u_t + g * u_s = - mu * u
#     for t in range(0, len(time) -1):

#         for s in range(1,len(size)): 
#             Ntemp = 0

#             # step 1 -- half time step
#             Ntemp = N[t,s] * np.exp(mu[s] * dt/2)

#             # step 2 -- time step 
#             Ntemp = N[t,s] - dt * ( g[s] * (N[t,s] - N[t,s-1])/ds )

#             # step 3 -- half time step
#             N[t+1,s] = Ntemp * np.exp(mu[s] * dt/2)



    total_population_initial = np.sum(N[0, :])
    total_population_middle = np.sum(N[int((Ntime-1)/2), :])
    total_population_final = np.sum(N[Ntime -1, :])
    print('total population at t = 0 : ' + str(total_population_initial))
    print('total population at t = '+ str(int(Ntime/2)) +' : ' + str(total_population_middle))
    print('total population at t = ' + str(Ntime) + ' : ' + str(total_population_final))

    totalPop = np.trapz(N[0,:])
    print(totalPop)



    for t_index, N_t in enumerate(N):
        # plt.plot(size, N_t, label=f'Numerical at time {t_index}', linestyle='--')
        if t_index % 100 == 0:  # Plot only if time index is a multiple of 10
            plt.plot(size, N_t, label=f'Numerical at time {t_index * dt}', linestyle='--')

    plt.axhline(y=1, color='r', linestyle='--', label='y=1')
    # plt.plot(size, N[3], label='Numerical', linestyle='--')
    # plt.axvline(x=0.4, color='r', linestyle='--', label='x=1')
    plt.xlabel('Size')
    plt.ylabel('Population')
    plt.title('Population by size')
    plt.legend()
    # plt.ylim(-.2, 1.4)  # Set y-axis limits from 0 to 12
    plt.show()


    plt.plot()



   # print(np.shape(N))
    # print(gp)
    # print(Ntime)
    # print(size)
    # print(np.shape(size))
    # print(np.shape(time))
    



