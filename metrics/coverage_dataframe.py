import pandas as pd

FILE_PATH = "fairness_project/outputs/pop/recommendations.json"

# load recommendations
df = pd.read_json(FILE_PATH)

# Count unique recommended items
unique_items = df["item_id"].nunique()

# recBole includes padding item 0
total_items = 1683 - 1

coverage = unique_items / total_items

print("Unique recommended items:", unique_items)
print("Coverage:", coverage)