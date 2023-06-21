import numpy as np

# Define the target values and threshold
target_values = [1, 2, 100]
threshold = 0.1  # Adjust the threshold as per your requirement

# Define the array
values = np.array([0, 2, 3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 3, 0, 0, 3, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 1, 0, 5, 3, 0, 0,
                   5, 0, 0, 0, 2, 0, 0, 3, 0, 0, 3, 0, 0, 2, 2, 0, 4, 3, 2, 0, 0, 0, 0, 0, 0, 2, 4, 0, 0, 2, 0, 4, 0, 5, 0, 0, 1,
                   0, 0, 0, 2, 3, 0, 0, 1, 4, 0, 2, 2, 0, 0, 0, 0, 0, 0, 4, 3, 0, 5, 0, 0, 0])

# Find values similar to the target values
similar_values = []
for value in values:
    for target in target_values:
        if abs(value - target) <= threshold:
            similar_values.append(value)

# Display the similar values
print("Similar Values:", similar_values)
