import numpy as np
nd9 = np.random.random([5,5])
np.savetxt(fname='./text1.txt',X = nd9)
nd10 = np.loadtxt('./text1.txt')
print(nd10)
