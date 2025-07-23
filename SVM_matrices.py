import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy import stats


from sklearn import datasets  # to retrieve the iris Dataset

data_cpu = {
    "Cores (number)": [8, 14, 20, 16, 8, 8, 18, 4, 20, 4],
    "Cache L3 (Mb)": [16.5, 19.25, 27.5, 22, 16, 12, 24.75, 8.25, 27.5, 8],
    "Performance (GFLOPS)": [
        973,
        1478.4,
        1536,
        1075.2,
        460.8,
        460.8,
        1324.8,
        460.8,
        1600,
        256,
    ],
    "Clock Speed (GHz)": [3.8, 3.3, 2.4, 2.1, 3.8, 3.8, 2.3, 3.6, 2.5, 4],
    'TDP': [150,125,165,140,140,165,75,140,45,15]
}

data_cpu_n = {'Cores (number)': [5120, 5120, 5120, 4352, 4608, 3584, 2944, 3840, 3840, 3840, 2560],
            'VRAM': [32, 32, 12, 11, 48, 11, 8, 24, 12, 24, 8],
            'Bandwidth (Gb/s)': [900, 868.4, 652.8, 616, 672, 484, 448, 432, 547.7, 346.1, 320],
            'Performance (TFLOPS)': [15.7, 16.66, 14.9, 13.45, 16.3, 11.3, 10.1, 12, 12.15, 12, 8.9]} #actually gpu


y_sc = [2508, 3262, 4190, 3698, 2402, 2480, 3032, 1761, 2978, 1400] #thats cpu
#y_sc = [35791, 33880, 33406, 32870, 27651, 24386, 23827, 21674, 20103, 18006, 17383]

df_val_transp = list(map(list, zip(*data_cpu.values())))

df = pd.DataFrame(df_val_transp, columns=data_cpu.keys())
#x = df["Cache L3 (Mb)"]
#x = df["VRAM"]
x = df["Clock Speed (GHz)"]
res = stats.pearsonr(x, y_sc)
# prin peron results probability/p-value
print(res)
df.head()
print(df)


# Standardize the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
scaled_data = pd.DataFrame(scaler.fit_transform(df))  # scaling the data
scaled_data

sns.heatmap(pd.DataFrame(df_scaled).corr())

# Check the Co-relation between features without PCA
sns.heatmap(
    scaled_data.corr(),
    annot=True,
    xticklabels=data_cpu.keys(),
    yticklabels=data_cpu.keys(),
)

exit

# Apply PCA to reduce to 2 components
pca = PCA(n_components=2)
principal_components = pca.fit_transform(df_scaled)

# Create a DataFrame with the principal components
df_pca = pd.DataFrame(data=principal_components, columns=["PC1", "PC2"])

#sns.heatmap(df_pca.corr())

# Print the explained variance ratio
print("Explained variance ratio of the 2 components:", pca.explained_variance_ratio_)
print("Principal components:\n", df_pca)


# Plot the data points
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(df_pca["PC1"], df_pca["PC2"], y_sc, color="blue")

# Add labels to the plot
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")


fig2 = go.Figure(
    data=[
        go.Mesh3d(
            x=df_pca["PC1"], y=df_pca["PC2"], z=y_sc, color="lightpink", opacity=0.50
        )
    ]
)



fig2.show()


# Show the plot
plt.show(block=True)