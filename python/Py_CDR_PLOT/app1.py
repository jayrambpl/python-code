import numpy as np
import matplotlib.pyplot as plt

# Load matrix data from CSV files, treat all data as strings
matrix1 = np.genfromtxt('matrix1.csv', delimiter=',', dtype='str')
matrix2 = np.genfromtxt('matrix2.csv', delimiter=',', dtype='str')

# Use the first row as headers
headers = matrix1[0, :]
matrix1 = matrix1[1:, :]
matrix2 = matrix2[1:, :]

# Find non-matching values
mismatch_matrix = matrix1 != matrix2

# Display the original matrices and the mismatch matrix
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nMismatch Matrix:")
print(mismatch_matrix)

# Plot the matrices and highlight mismatch points
plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.title('Matrix 1')
plt.imshow(mismatch_matrix, cmap='viridis', interpolation='none', origin='upper', aspect='auto')

plt.xticks(np.arange(len(headers)), headers, rotation=45, ha='right')
plt.yticks(np.arange(matrix1.shape[0]), np.arange(1, matrix1.shape[0] + 1))

# Plot the matrices and highlight mismatch points
plt.subplot(132)
plt.title('Matrix 2')
plt.imshow(mismatch_matrix, cmap='viridis', interpolation='none', origin='upper', aspect='auto')

plt.xticks(np.arange(len(headers)), headers, rotation=45, ha='right')
plt.yticks(np.arange(matrix1.shape[0]), np.arange(1, matrix1.shape[0] + 1))

# Plot the mismatch matrix
plt.subplot(133)
plt.title('Mismatch Matrix')
plt.imshow(mismatch_matrix, cmap='Reds', interpolation='none', origin='upper', aspect='auto')

plt.xticks(np.arange(len(headers)), headers, rotation=45, ha='right')
plt.yticks(np.arange(matrix1.shape[0]), np.arange(1, matrix1.shape[0] + 1))

# Highlight mismatch points
for i in range(matrix1.shape[0]):
    for j in range(matrix1.shape[1]):
        if mismatch_matrix[i, j]:
            plt.text(j, i, 'X', ha='center', va='center', color='black')

plt.tight_layout()
plt.show()
