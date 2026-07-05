def get_number_of_items(dataset):

    # subtract padding item 0
    return dataset.item_num - 1


def get_number_of_users(dataset):

    # subtract padding user 0
    return dataset.user_num - 1