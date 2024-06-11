import numpy as np


python_list = [1,2,3,4,5,6]

np_array = np.array([1,2,3,4,5,6])

# print(type(python_list))
# print(type(np_array))

python_multi = [[1,2],[3,4],[5,6]]
np_multi = np_array.reshape(3,2)

print(python_multi)
print(np_multi)
