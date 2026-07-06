from recbole.quick_start import load_data_and_model
from recbole.data.interaction import Interaction

import pandas as pd
import torch


def extract_recommendations_recbole(
    model_path,
    top_k=10
):

    config, model, dataset, train_data, valid_data, test_data = (
        load_data_and_model(
            model_file=model_path
        )
    )

    model.eval()

    all_rows = []

    for user_id in range(1, dataset.user_num):

        interaction = Interaction({
            "user_id": torch.tensor([user_id])
        })

        scores = model.full_sort_predict(interaction)

        top_scores, top_items = torch.topk(
            scores,
            top_k
        )

        for rank, (item, score) in enumerate(
            zip(top_items.tolist(), top_scores.tolist()),
            start=1
        ):

            all_rows.append({
                "user_id": user_id,
                "item_id": int(item),
                "rank_position": rank,
                "predicted_score": float(score)
            })

    df = pd.DataFrame(all_rows)

    return df, dataset


def get_number_of_items(dataset):

    return dataset.item_num - 1


def get_number_of_users(dataset):

    return dataset.user_num - 1