import numpy as np

array_sizes = np.random.choice(range(3, 11), size=5, replace=False)  #1~10 사이
arrays = []

for size in array_sizes:
    array = np.random.randint(1, 11, size=size)  # 1~10 사이 값
    array.sort()
    arrays.append(array)

# Print the arrays
# for i, array in enumerate(arrays):
#     print(f"Array {i+1}: {array}")
print(array_sizes)