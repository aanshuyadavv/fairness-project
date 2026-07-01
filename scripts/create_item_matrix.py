import pandas as pd
import numpy as np

# load recommendations
df = pd.read_json(
    "fairness_project/outputs/pop/recommendations.json"
)

# Number of users
num_users = df["user_id"].nunique()

# Top-K size
TOP_K = df["rank_position"].max()

# Create empty matrix
item_matrix = np.zeros((num_users, TOP_K), dtype=int)

# Fill matrix
for _, row in df.iterrows():

    user_idx = int(row["user_id"]) - 1
    rank_idx = int(row["rank_position"]) - 1

    item_matrix[user_idx][rank_idx] = int(row["item_id"])

print(item_matrix)

# Save matrix
np.save(
    "fairness_project/outputs/pop/item_matrix.npy",
    item_matrix
)

print("\nItem matrix saved successfully!")