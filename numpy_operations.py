import numpy as np

numbers1 = np.random.randint(1,100,6)
numbers2 = np.random.randint(1,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2
result = numbers1 + 10
result = numbers1 - numbers2
result = numbers1 * numbers2
result = numbers1 / numbers2
result = numbers1 / 2

result = np.sin(numbers1)
result = np.cos(numbers2)
result = np.sqrt(numbers1)
result = np.log(numbers2)

multi_numbers1 = numbers1.reshape(2,3)
multi_numbers2 = numbers2.reshape(2,3)

print(multi_numbers1)
print(multi_numbers2)

print(result)