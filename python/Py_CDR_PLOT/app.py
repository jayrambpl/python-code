import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load matrix data from CSV files, treat all data as strings
matrix1 = np.genfromtxt('1943.csv', delimiter=',', dtype='str')
matrix2 = np.genfromtxt('1943_1.csv', delimiter=',', dtype='str')

# Use the first row as headers
headers = matrix1[0, :]
matrix1 = matrix1[1:, :]
matrix2 = matrix2[1:, :]

# Find non-matching values
mismatch_matrix = matrix1 != matrix2

# Create a DataFrame for Seaborn
df_mismatch = pd.DataFrame(mismatch_matrix.astype(int), columns=headers)

# Set up Seaborn style
sns.set(style="whitegrid")

# Plot the mismatch matrix using Seaborn heatmap with annotations
plt.figure(figsize=(12, 4))

plt.subplot(131)
sns.heatmap(df_mismatch, cmap='viridis', annot=False, cbar=False, linewidths=.5, square=True)
plt.title('Matrix 1')

# Annotate mismatch points with header and row number
for i in range(matrix1.shape[0]):
    for j in range(matrix1.shape[1]):
        if mismatch_matrix[i, j]:
            plt.text(j + 0.5, i + 0.5, f'({headers[j]}, {i + 1})', ha='center', va='center', fontsize=8, color='black')

plt.subplot(132)
sns.heatmap(df_mismatch, cmap='viridis', annot=False, cbar=False, linewidths=.5, square=True)
plt.title('Matrix 2')

# Annotate mismatch points with header and row number
for i in range(matrix1.shape[0]):
    for j in range(matrix1.shape[1]):
        if mismatch_matrix[i, j]:
            plt.text(j + 0.5, i + 0.5, f'({headers[j]}, {i + 1})', ha='center', va='center', fontsize=8, color='black')

plt.subplot(133)
sns.heatmap(df_mismatch, cmap='Reds', annot=False, cbar=False, linewidths=.5, square=True)
plt.title('Mismatch Matrix')

# Annotate mismatch points with header and row number
for i in range(matrix1.shape[0]):
    for j in range(matrix1.shape[1]):
        if mismatch_matrix[i, j]:
            plt.text(j + 0.5, i + 0.5, f'({headers[j]}, {i + 1})', ha='center', va='center', fontsize=8, color='black')

plt.tight_layout()
plt.show()
