import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import MDS
from sklearn.metrics import pairwise_distances

# Load your data
file_path = 'cars.csv'
df = pd.read_csv(file_path)

# Keep only numerical attributes
numerical_cols = ['wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight', 
                  'enginesize', 'boreratio', 'stroke', 'compressionratio', 'horsepower', 
                  'peakrpm', 'citympg', 'highwaympg', 'price']
df_numerical = df[numerical_cols]

# Compute the correlation matrix
correlation_matrix = df_numerical.corr()
correlation_matrix.to_csv('correlation_matrix.csv')

# Compute ordered attributes for Parallel Coordinates
correlation_matrix_abs = correlation_matrix.abs()
correlation_sums = correlation_matrix_abs.sum().sort_values(ascending=False)
ordered_attributes = [correlation_sums.index[0]]
while len(ordered_attributes) < 8:
    last_attr = ordered_attributes[-1]
    next_attr = correlation_matrix_abs[last_attr].drop(ordered_attributes).idxmax()
    ordered_attributes.append(next_attr)

# Save ordered data for D3
ordered_df = df[ordered_attributes]
ordered_df.to_csv('ordered_data.csv', index=False)

# Select the top categorical variables based on correlation strength with numerical attributes
categorical_col = ['carbody', 'drivewheel']
ordered_df[categorical_col] = df[categorical_col]

# Reduce data points to a manageable size
df_reduced = df.sample(n=100)  # Adjust sample size as needed

# Filter only the selected columns
df_filtered = df_reduced[categorical_col + numerical_cols]

# Save to CSV
df_filtered.to_csv('filtered_data_with_categorical.csv', index=False)
ordered_df.to_csv('ordered_data_with_categorical.csv', index=False)

# Select top 5 attributes for scatterplot matrix
top_attributes = correlation_sums.index[:5]

# Select top 5 numerical attributes
top_numerical_attributes = correlation_sums.index[:5].tolist()

# Save the data for the scatterplot matrix
scatter_data = df[top_attributes]
scatter_data.to_csv('scatter_data.csv', index=False)

# Standardize the data
scaler = StandardScaler()
standardized_data = scaler.fit_transform(df_numerical)

# Perform PCA
pca = PCA(n_components=8)
principal_components = pca.fit_transform(standardized_data)

# Get explained variance
explained_variance = pca.explained_variance_

# Save the PCA results
df_pca = pd.DataFrame(data=principal_components, columns=[f'PC{i+1}' for i in range(principal_components.shape[1])])
df_pca.to_csv('pca_data.csv', index=False)

# Save the explained variance
df_variance = pd.DataFrame(data=explained_variance, columns=['Variance'])
df_variance.to_csv('variance_data.csv', index=False)

# Compute PCA loadings (eigenvectors)
loadings = pca.components_.T

# Add variable names for labeling
loadings_df = pd.DataFrame(loadings, columns=[f'PC{i+1}' for i in range(loadings.shape[1])])
loadings_df['variable'] = numerical_cols

# Save only the first two components for the biplot
df_loadings = loadings_df[['PC1', 'PC2', 'variable']].head(8)  # Limit to top 8 attributes
df_loadings.to_csv('biplot_loadings.csv', index=False)

# Save the PCA scores for biplot
df_scores = pd.DataFrame(data=principal_components[:, :2], columns=['PC1', 'PC2'])
df_scores.to_csv('biplot_scores.csv', index=False)

# MDS display of the data (Euclidean distance)
distance_matrix = pairwise_distances(standardized_data, metric='euclidean')
mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
mds_result = mds.fit_transform(distance_matrix)
df_mds = pd.DataFrame(data=mds_result, columns=['Dim1', 'Dim2'])
df_mds.to_csv('mds_data.csv', index=False)

# MDS display of the attributes (1 - |correlation| distance)
distance_matrix_corr = 1 - correlation_matrix_abs
mds_corr = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
mds_result_corr = mds_corr.fit_transform(distance_matrix_corr)
df_mds_corr = pd.DataFrame(data=mds_result_corr, columns=['Dim1', 'Dim2'], index=numerical_cols)
df_mds_corr.to_csv('mds_attributes.csv')

# Select top 5 numerical attributes
top_numerical_attributes = correlation_sums.index[:5].tolist()

# Add 2 categorical variables of your choice
categorical_cols = ['drivewheel', 'carbody']
selected_cols = top_numerical_attributes + categorical_cols

# Create a new DataFrame with selected columns
df_selected = df[selected_cols]

# Save the data for the 7x7 scatter plot matrix
df_selected.to_csv('scatter_data_with_categorical.csv', index=False)
