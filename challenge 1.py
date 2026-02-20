import pandas as pd
import matplotlib.pyplot as plt

# Load files
height_df = pd.read_csv("height.csv")
weight_df = pd.read_csv("weight.csv")

# Preview data
print(height_df.head())
print(weight_df.head())

# IQR for Weight
Q1_w = weight_df['Weight'].quantile(0.25)
Q3_w = weight_df['Weight'].quantile(0.75)
IQR_w = Q3_w - Q1_w

lower_w = Q1_w - 1.5 * IQR_w
upper_w = Q3_w + 1.5 * IQR_w

# Outliers
weight_outliers = weight_df[
    (weight_df['Weight'] < lower_w) |
    (weight_df['Weight'] > upper_w)
]

print("Weight Outliers:")
print(weight_outliers)
print("Total:", len(weight_outliers))

# IQR for Height
Q1_h = height_df['Height'].quantile(0.25)
Q3_h = height_df['Height'].quantile(0.75)
IQR_h = Q3_h - Q1_h

lower_h = Q1_h - 1.5 * IQR_h
upper_h = Q3_h + 1.5 * IQR_h

# Outliers
height_outliers = height_df[
    (height_df['Height'] < lower_h) |
    (height_df['Height'] > upper_h)
]

print("Height Outliers:")
print(height_outliers)
print("Total:", len(height_outliers))

df = pd.concat([height_df, weight_df], axis=1)
print(df.head())



# Histograms
plt.figure(figsize=(12,5))

# Height histogram
plt.subplot(1,2,1)
plt.hist(height_df['Height'], bins=30)
plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")

# Weight histogram
plt.subplot(1,2,2)
plt.hist(weight_df['Weight'], bins=30)
plt.title("Weight Distribution")
plt.xlabel("Weight")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

