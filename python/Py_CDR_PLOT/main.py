import numpy as np
import pandas as pd
import seaborn as sns
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

# Create a DataFrame for Seaborn
df_mismatch = pd.DataFrame(mismatch_matrix.astype(int), columns=headers)

# Set up Seaborn style
sns.set(style="whitegrid")

# Set the figure size to 10x12 inches
fig, ax = plt.subplots(figsize=(12, 10))

# Annotate mismatch points with header, row number, old value, and new value
for i in range(matrix1.shape[0]):
    for j in range(matrix1.shape[1]):
        if mismatch_matrix[i, j]:
            old_value = matrix1[i, j]
            new_value = matrix2[i, j]
            annotation_text = f'Row: {i + 1}, Col: {headers[j]}, Before: {old_value}, After: {new_value}'
            print(annotation_text)
            ax.text(j, i, annotation_text, ha='center', va='center', fontsize=6, color='black')

# Plot the mismatch matrix
plt.imshow(df_mismatch, cmap='Reds', interpolation='none', origin='upper', aspect='auto')            
# sns.heatmap(df_mismatch, cmap='Reds', annot=False, cbar=False, linewidths=.5, square=True, ax=ax)

# Set x and y axis ticks
ax.set_xticks(np.arange(len(headers)) + 0.5)
ax.set_yticks(np.arange(matrix1.shape[0]) + 0.5)
ax.set_xticklabels(headers, rotation=45, ha='right', fontsize=6)
ax.set_yticklabels(np.arange(1, matrix1.shape[0] + 1), fontsize=6)

plt.title('CDR Mismatch')
plt.show()
