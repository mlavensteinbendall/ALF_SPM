import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt
from function_upwind import UPW_SPM

def conservation_plt(data, size, time, ds):

    totalPop_num = np.zeros([len(time)])
    totalPop_sol = np.zeros([len(time)])

     #analytical solution 
    sol = np.zeros([len(time),len(size)])

    for t in range(0, len(time)):
        for s in range(0, len(size)):
            # Calculate the analytical solution
            c = 1/10
            Y = 1/c * np.log(np.exp(size[s]*c) - time[t]*c)  # g(s) = exp(-s/10)
            phi = np.exp(-((Y - 5) / 1) ** 2)
            sol[t,s] = phi * np.exp( c**2 * (Y -  np.log( c*time[t] + np.exp(Y) ) ) ) # g(s) = exp(-s/10), mu(s) = 0

    print(np.shape(data))

    for t in range(len(time)):
        totalPop_num[t] = ds * np.sum(data[t,:])
        totalPop_sol[t] = ds * np.sum(sol[t,:])

    # Plot total population over time
    plt.plot(time, totalPop_num)
    plt.xlabel('Time')
    plt.ylabel('total pop')
    plt.title('Total Population over Time')
    # plt.grid(True)
    plt.show()

    # Calculate the absolute error at each time t
    error = np.abs(( totalPop_num - totalPop_sol)) 

    # Checks (optional)
    # print(error)
    # print('numerical t end : ' + str(totalPop_num[-1]))
    # print('analytical t end : ' + str(totalPop_sol[-1]))

    # Plot absolute error oftotal population over time
    plt.plot(time, error)
    plt.xlabel('Time')
    plt.ylabel('Absolute Error |numerical - true solution|')
    plt.title('Error of Total Population over Time')
    # plt.grid(True)
    plt.show()