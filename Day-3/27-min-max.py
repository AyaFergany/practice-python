import numpy as np

N, M = list(map(int, input().split()))
arr=np.array([[int(x) for x in input().split()] for i in range(N)])
arr_min = np.min(arr, axis=1)
print(np.max(arr_min))

