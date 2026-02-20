import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

df = pd.read_csv("bhp.csv")

print(df.head())
print(df.shape)

lower_percentile = df['price_per_sqft'].quantile(0.001)
upper_percentile = df['price_per_sqft'].quantile(0.999)

print("Lower bound:", lower_percentile)
print("Upper bound:", upper_percentile)

# Filter dataframe
df_percentile = df[
    (df['price_per_sqft'] >= lower_percentile) &
    (df['price_per_sqft'] <= upper_percentile)
]

print("Shape after percentile outlier removal:", df_percentile.shape)

mean = df_percentile['price_per_sqft'].mean()
std = df_percentile['price_per_sqft'].std()

print("Mean:", mean)
print("Std Dev:", std)

lower_limit = mean - 4 * std
upper_limit = mean + 4 * std

df_std = df_percentile[
    (df_percentile['price_per_sqft'] >= lower_limit) &
    (df_percentile['price_per_sqft'] <= upper_limit)
]

print("Shape after std dev filtering:", df_std.shape)

plt.figure(figsize=(10,6))

# Histogram
count, bins, ignored = plt.hist(
    df_std['price_per_sqft'],
    bins=50,
    density=True,
    alpha=0.6
)

# Bell curve
mu = df_std['price_per_sqft'].mean()
sigma = df_std['price_per_sqft'].std()

x = np.linspace(bins.min(), bins.max(), 100)
plt.plot(x, norm.pdf(x, mu, sigma), linewidth=2)

plt.title("Histogram with Bell Curve (After Outlier Removal)")
plt.xlabel("Price per Sqft")
plt.ylabel("Density")

plt.show()

# Calculate z-score
df_percentile['zscore'] = (
    (df_percentile['price_per_sqft'] - mean) / std
)

# Filter using zscore
df_z = df_percentile[
    (df_percentile['zscore'] <= 4) &
    (df_percentile['zscore'] >= -4)
]

print("Shape after z-score filtering:", df_z.shape)
