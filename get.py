import numpy as np
nd = np.random.random([10])
print(nd)
# nd1 = np.random.random((2,10))
# print(nd1)


nd2 = np.arange(100).reshape([10,10])
print(nd2)
# print(nd2[1:3,:])
# print(nd2[(nd2>3)&(nd2<10)])
print(nd2[2::2,::3])
