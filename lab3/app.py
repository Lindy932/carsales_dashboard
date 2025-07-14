import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import MDS
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load your data
file_path = 'cars.csv'
df = pd.read_csv(file_path)

# Ensure 'car_ID' is included 
if 'car_ID' not in df.columns:
    raise KeyError("Column 'car_ID' not found in the dataset.")

# Keep only numerical attributes and 'car_ID'
numerical_cols = ['wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight', 
                  'enginesize', 'horsepower', 'highwaympg']
df_numerical = df[numerical_cols + ['car_ID']]

# Standardize the data
scaler = StandardScaler()
standardized_data = scaler.fit_transform(df_numerical.drop(columns=['car_ID']))

# Perform PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(standardized_data)

# Save the PCA results (PC scores)
df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
df_pca['car_ID'] = df_numerical['car_ID'].values
df_pca.to_csv('biplot_scores.csv', index=False)

# save the PCA results for the variance percentages
# Save the PCA results (PC scores)
explained_variance_ratio = pca.explained_variance_ratio_

df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
df_pca['car_ID'] = df_numerical['car_ID'].values
df_pca.to_csv('biplot_scores.csv', index=False)

# Save explained variance ratio
df_variance = pd.DataFrame({'PC': ['PC1', 'PC2'], 'Variance': explained_variance_ratio})
df_variance.to_csv('explained_variance.csv', index=False)
###

# Calculate and save PCA loadings (contribution of each feature to the principal components)
pca_loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2'], index=numerical_cols)
pca_loadings.reset_index(inplace=True)
pca_loadings.rename(columns={'index': 'attribute'}, inplace=True)
pca_loadings.to_csv('biplot_loadings.csv', index=False)

# Perform MDS
mds = MDS(n_components=2, random_state=42)
mds_fit = mds.fit_transform(standardized_data)

# Save MDS results
df_mds = pd.DataFrame(data=mds_fit, columns=['MDS1', 'MDS2'])
df_mds['car_ID'] = df_numerical['car_ID'].values
df_mds.to_csv('mds_scores.csv', index=False)

# Elbow Method
def elbow_method(X):
    distortions = []
    K = range(1, 11)
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        distortions.append(kmeans.inertia_)
    return K, distortions

K, distortions = elbow_method(standardized_data)

# Save the elbow method results (Source: MicroSoft CoPilot.com)
df_elbow = pd.DataFrame({'k': K, 'distortion': distortions})
df_elbow.to_csv('elbow_method.csv', index=False)

# Plot the elbow method results
plt.figure(figsize=(8, 4))
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('Elbow Method For Optimal k')
plt.savefig('elbow_method.png')
plt.show()

# Optimal number of clusters which will be updated based on elbow method
optimal_k = 4

# Perform K-means clustering
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(standardized_data)

# Save the clustering results
df_numerical['cluster'] = clusters
df_numerical.to_csv('kmeans_clusters.csv', index=False)
