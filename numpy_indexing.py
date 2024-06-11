import numpy as np

numbers = np.array([1,3,5,6,8,9,13,15])

result = numbers[3]
result = numbers[-1]
result = numbers[0:4]
result = numbers[:3]
result = numbers[4:]
result = numbers[::]
result = numbers[::-2]

print(result)