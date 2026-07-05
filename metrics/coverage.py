def coverage(df, total_items):

    unique_items = df["item_id"].nunique()

    coverage = unique_items / total_items

    return unique_items, coverage