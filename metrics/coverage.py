import numpy as np


def compute_coverage(item_matrix, total_items):

    unique_items = np.unique(item_matrix)

    coverage = len(unique_items) / total_items

    return len(unique_items), coverage


# load item matrix
item_matrix = np.load(
    "fairness_project/outputs/pop/item_matrix.npy"
)

TOTAL_ITEMS = 1682

unique_items, coverage = compute_coverage(
    item_matrix,
    TOTAL_ITEMS
)

print("Unique recommended items:", unique_items)
print("Coverage:", coverage)