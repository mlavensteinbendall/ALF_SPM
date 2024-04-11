# Current state
# d/dt(N) + d/ds (g(s)N) = mu N
# mu(s) = 0
# g(s) = exp(-s/10)


import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

def UPW_SPM(size, time, ds, dt):

# initial conditions -- eventually will move to main file
    # growth rate
    g = np.zeros([len(size)])
    g[:] = np.exp(-size[:]/10) 

    # mortality rate
    mu = np.zeros([len(size)])
    # mu = size

    # analytical derivative of growth rate !! ignore for right now !!
    gp = np.zeros([len(size)])
    gp[:] = - g[:]/10

    # inital condition -- population at t=0
    N = np.zeros([len(time),len(size)])
    N[0,:] = np.exp(-(size[:]-5)**2)

    #analytical solution 
    sol = np.zeros([len(time),len(size)])


# WITH gp - Steve's time splitting  on u_t + (g * u)_s = -mu * u
    for t in range(0, len(time) - 1):

        for s in range(1,len(size)): 
            Ntemp = 0

            # step 1 -- half time step
            Ntemp = N[t,s] * np.exp(mu[s] * dt/2)

            # step 2 -- time step 
            Ntemp = Ntemp - dt * ((g[s]*(Ntemp - N[t,s-1])/ds) + gp[s]* Ntemp)

            # step 3 -- half time step
            N[t+1,s] = Ntemp * np.exp(mu[s] * dt/2)


    for t in range(0, len(time)):
        for s in range(0, len(size)):
            # Calculate the analytical solution
            c = 1/10
            Y = 1/c * np.log(np.exp(size[s]*c) - time[t]*c)  # g(s) = exp(-s/10)
            phi = np.exp(-((Y - 5) / 1) ** 2)
            sol[t,s] = phi * np.exp( c**2 * (Y -  np.log( c*time[t] + np.exp(Y) ) ) ) # g(s) = exp(-s/10), mu(s) = 0



# # WITH gp - on the board time splitting
#     for t in range(0, len(time) - 1):

#         for s in range(1,len(size)): 
#             Ntemp = 0

#             # step 1 -- half time step
#             Ntemp = N[t,s] * np.exp( ( - mu[s] - gp[s] ) * dt / 2 )

#             # step 2 -- time step 
#             Ntemp = Ntemp - dt * ( g[s] * ( Ntemp - N[t,s-1] ) / ds ) 

#             # step 3 -- half time step
#             N[t+1,s] = Ntemp * np.exp( ( - mu[s] - gp[s] ) * dt / 2 )








# Plots the numerical solution at multiple points in time
    for t_index, N_t in enumerate(N):
        if t_index % 100 == 0:  # Plot only if time index is a multiple of 10
            plt.plot(size, N_t, label=f'Numerical at time {t_index * dt}', linestyle='--')
    
    # for t_index, sol_t in enumerate(sol):
    #     if t_index % 100 == 0:  # Plot only if time index is a multiple of 10
    #         plt.plot(size, sol_t, label=f'Analytical at time {t_index * dt}', linestyle='-')

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







# MOOOVVVE TO CONSERVATION FILE
# check conservation -- need to have ds * sum
    # total_population = np.zeros([len(time)])
    # total_population = size[-1] * np.sum(N, axis=1)
    # # max_population_index = np.argmax(total_population)
    # # print(max_population_index)

    # # print(total_population)



    # # Plot total population over time
    # plt.plot(time, total_population)
    # plt.xlabel('Time')
    # plt.ylabel('Total Population')
    # plt.title('Total Population over Time')
    # # plt.grid(True)
    # plt.show()

    # totalPop_num = np.zeros([len(time)])
    # totalPop_sol = np.zeros([len(time)])

    # for t in range(len(time)):
    #     totalPop_num[t] = ds * np.sum(N[t,:])
    #     totalPop_sol[t] = ds * np.sum(sol[t,:])

    # error = np.abs(( totalPop_num - totalPop_sol)) 
    # print(error)
    # print('numerical t end : ' + str(totalPop_num[-1]))
    # print('analytical t end : ' + str(totalPop_sol[-1]))

    # # Plot total population over time
    # plt.plot(time, error)
    # plt.xlabel('Time')
    # plt.ylabel('Absolute Error |numerical - true solution|')
    # plt.title('Error of Total Population over Time')
    # # plt.grid(True)
    # plt.show()

    # plt.plot(time, totalPop_num)
    # plt.xlabel('Time')
    # plt.ylabel('total pop')
    # plt.title('Total Population over Time')
    # # plt.grid(True)
    # plt.show()

    return N
    







# WITH gp - on the board time splitting
    # for t in range(0, len(time) -1):

    #     for s in range(1,len(size)): 
    #         Ntemp = 0

    #         # step 1 -- half time step
    #         Ntemp = N[t,s] * np.exp( ( -mu[s] - gp[s] )* dt/2 )

    #         # step 2 -- time step 
    #         Ntemp = N[t,s] - dt * ( g[s] * (N[t,s] - N[t,s-1])/ds ) 

    #         # step 3 -- half time step
    #         N[t+1,s] = Ntemp * np.exp(( -mu[s] - gp[s] ) * dt/2)

# # WITHOUT gp --  time splitting with u_t + g * u_s = - mu * u 
#     for t in range(0, len(time) -1):

#         for s in range(1,len(size)): 
#             Ntemp = 0

#             # step 1 -- half time step
#             Ntemp = N[t,s] * np.exp(mu[s] * dt/2)

#             # step 2 -- time step 
#             Ntemp = N[t,s] - dt * ( g[s] * (N[t,s] - N[t,s-1])/ds )

#             # step 3 -- half time step
#             N[t+1,s] = Ntemp * np.exp(mu[s] * dt/2)



# # Total Population - this is to check if the solution is conservative when we have no death or births
#     total_population_initial = np.sum(N[0, :])
#     total_population_middle = np.sum(N[int((len(time)-1)/2), :])
#     total_population_final = np.sum(N[len(time) -1, :])

#     print('total population at t = 0 : ' + str(total_population_initial))
#     print('total population at t = '+ str(int(len(time)/2)) +' : ' + str(total_population_middle))
#     print('total population at t = ' + str(len(time)) + ' : ' + str(total_population_final))

