import numpy as np # Numpy for numpy
import matplotlib.pyplot as plt
from function_upwind_size import UPW_SPM

def trapezoidal_rule(fx, dx):

    fx_sum = np.sum(fx[1:-1])

    result = dx * ( (fx[0] + fx[-1]) / 2 + fx_sum)

    return result


def conservation_plt(data, size, time, ds):

    totalPop_num = np.zeros([len(time)])
    totalPop_sol = np.zeros([len(time)])

    # analytical solution 
    sol = np.zeros([len(time),len(size)])

    c = 1
    for i_t in range(0, len(time)):
        # Calculate the analytical solution
        sol[i_t,:] = np.exp(-(size - ( time[i_t] + 5))**2) * np.exp(-c * time[i_t]) # mu(s) = 0


    for t in range(len(time)):
        # totalPop_num[t] = ds * np.sum(data[t,:])
        # totalPop_sol[t] = ds * np.sum(sol[t,:])

        # totalPop_num[t] = np.trapz(data[t,:], size, ds)
        # totalPop_sol[t] = np.trapz(sol[t,:], size, ds)

        totalPop_num[t] = trapezoidal_rule(data[t,:], ds)
        totalPop_sol[t] = trapezoidal_rule(sol[t,:], ds)

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
