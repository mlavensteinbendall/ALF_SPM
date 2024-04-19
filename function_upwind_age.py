# Current state
# d/dt(N) + d/ds (g(s)N) = mu N
# mu(s) = 0
# g(s) = exp(-s/10)


import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt

def UPW_SPM(age, time, da, dt, order):

    # mortality rate
    mu = np.zeros([len(age)])

    # inital condition -- population at t=0
    N = np.zeros([len(time),len(age)])
    N[0,:] = np.exp(-(age[:]-5)**2)


    if order == 1:
        for t in range(0, len(time) - 1):

            for a in range(1,len(age)): 
                
                # Time Splitting
                    Ntemp = N[t,a]

                    # step 1 -- half time step
                    Ntemp -= (dt/(2*da)) * (N[t,a] - N[t,a-1])

                    # step 2 -- time step 
                    Ntemp -= dt * mu[a] * Ntemp

                    # step 3 -- half time step
                    N[t+1,a] = Ntemp - (dt/(2*da)) * (N[t,a] - N[t,a-1])
                    
                    
                    # without time-splitting
                    # N[t+1,a] = N[t,a] - dt *( ( (N[t,a] - N[t,a-1]) / da ) + mu[a] * N[t,a] ) # first order upwind method
    dtda = dt/da 

    if order == 2:
         
        # # Second-order upwind scheme to solve the PDE
        # for t in range(len(time) - 1):
        #     for i in range(2, len(age)):
        #         # Second-order upwind difference for spatial derivative
        #         dNda = (3*N[t, i] - 4*N[t, i-1] + N[t, i-2]) / (2 * da)
        #         # Time derivative and decay
        #         dNdt = -dNda - mu[i] * N[t, i]
        #         # Update using Euler's method
        #         N[t+1, i] = N[t, i] + dt * dNdt

        #     # Boundary conditions, assuming no flux at the boundary
        #     N[t+1, 0] = N[t+1, 1]  # Reflective or no-flux boundary condition at a_min
        #     N[t+1, 1] = N[t+1, 2]  # This can be adjusted based on physical assumptions


        for t in range(0, len(time) - 1):
            if t == 0:
                  for a in range(1,len(age)):    
                    N[t+1,a] = N[t,a] - dt *( ( (N[t,a] - N[t,a-1]) / da ) + mu[a] * N[t,a] ) # first order upwind method
            else:    
                for a in range(2,len(age)):  
                    dNda = 0
                    dNda = (3 * N[t,a] - 4 * N[t,a-1] + N[t,a-2])/ (2*da)

                    dNdt = dNda + mu[a] * N[t,a]

                    N[t+1,a] = N[t,a] - dt * dNdt

                    # # N[t+2,a] = 3 * N[t,a] - 4 * N[t+1,a] - 2 * dt * ((3 * N[t,a] - 4 * N[t,a-1] + N[t,a-2])/ (2*da) + mu[a]* N[t,a])
                    # N[t+1,a] = - ((3 - 3*dtda - 2*dt*mu[a]) * N[t-1,a] - 4 * N[t,a] + 4 * dtda * N[t-1,a-1]  - dtda *  N[t-1,a-2])
                
                N[t+1,0] = N[t+1,1]
                N[t+1,1] = N[t+1,2]

    # if order == 2:
    #     for t in range(0, len(time) - 2):
    #         if t == 0:
    #             for a in range(1, len(age)):
    #                 N[t+1, a] = N[t, a] - dt * ((N[t, a] - N[t, a-1]) / da + mu[a] * N[t, a])
    #         else:
    #             for a in range(2, len(age)):
    #                 # Apply the second-order upwind discretization
    #                 advection_term = (3 * N[t, a] - 4 * N[t, a-1] + N[t, a-2]) / (2 * da)
    #                 N[t+1, a] = N[t, a] - dt * (advection_term + mu[a] * N[t, a])
                    
                
    return N