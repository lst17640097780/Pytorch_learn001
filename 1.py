# 将列表转换成ndarray:
# import numpy as np
# lst1 = [3.14, 2.17, 0, 1, 2]
# nd1 =np.array(lst1)
# print(nd1)
# # [3.14 2.17 0. 1. 2. ]
# print(type(nd1))   类型
# # <class 'numpy.ndarray'>


# 嵌套列表可以转换成多维ndarray：
# import numpy as np
# lst2 = [[3.14, 2.17, 0, 1, 2], [1, 2, 3, 4, 5]]
# nd2 =np.array(lst2)
# print(nd2)
# # [[3.14 2.17 0. 1. 2. ]
# # [1. 2. 3. 4. 5. ]]
# print(type(nd2))
# # <class 'numpy.ndarray'>


# np.random.random的用法
# import numpy as np
# nd3 = np.random.random([1, 1])
# print(nd3)
# print('nd3的形状为：', nd3.shape)

#
# import numpy as np
# np.random.seed(123)
# nd4 = np.random.randn(2,3)   #标准正态随机数
# print(nd4)
# np.random.shuffle(nd4)
# print("随机打乱后数据:")
# print(nd4)
# print(type(nd4))


# import numpy as np  #结论：np.random.randint  只能得到一个整数，并不能得到矩阵
# nd = np.random.randint(2, 3)
# print(nd)


import numpy as np
# 生成全是 0 的 3x3 矩阵
nd5 =np.zeros([3, 3])
#生成与nd5形状一样的全0矩阵
#np.zeros_like(nd5)
# 生成全是 1 的 3x3 矩阵
nd6 = np.ones([3, 3])
# 生成 3 阶的单位矩阵
nd7 = np.eye(3)
# 生成 3 阶对角矩阵
nd8 = np.diag([1, 5, 3])
print(nd5)
# [[0. 0. 0.]
# [0. 0. 0.]
# [0. 0. 0.]]
print(nd6)
# [[1. 1. 1.]
# [1. 1. 1.]
# [1. 1. 1.]]
print(nd7)
# [[1. 0. 0.]
# [0. 1. 0.]
# [0. 0. 1.]]
print(nd8)
# [[1 0 0]
# [0 5 0]
# [0 0 3]]

nd8_5 = np.empty((2,3))
print(nd8_5)

