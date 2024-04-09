# Author: Morgan Lavenstein Bendall
# Objective: This calls the function of our model and runs at different ds and dt.

import numpy as np
from function_upwind import UPW_SPM

# initial conditions
Smax = 15
Tmax = 2

# ds = 0.1
dt = 0.01
# ds = np.zeros([1])
# ds[0] = 0.9 * dt
ds = 0.9 * dt
testN = 0
filename = 'test'

# for i in range(len(ds)):
#     UPW_SPM(Smax, Tmax, ds[i], dt, testN, filename)


UPW_SPM(Smax, Tmax, ds, dt, testN, filename)