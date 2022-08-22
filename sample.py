import numpy as np
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
idxs = np.random.randint(0, len(l), size=5) # 生成长度为5的随机数组，范围为 [0,10)，作为索引
print([l[i] for i in idxs]) # 按照索引，去l中获取到对应的值