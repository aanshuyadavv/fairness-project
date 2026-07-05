import numpy as np


def compute_coverage_matrix(item_matrix, total_items):

    unique_items = np.unique(item_matrix)

    coverage = len(unique_items) / total_items

    return len(unique_items), coverage