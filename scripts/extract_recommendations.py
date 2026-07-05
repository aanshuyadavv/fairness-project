import pandas as pd
import torch

from recbole.data.interaction import Interaction


def extract_recommendations_recbole(model, dataset, top_k=10):

    model.eval()

    all_rows = []

    # loop through users
    for user_id in range(1, dataset.user_num):

        interaction = Interaction({
            "user_id": torch.tensor([user_id])
        })

        scores = model.full_sort_predict(interaction)

        top_scores, top_items = torch.topk(scores, top_k)

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

    return pd.DataFrame(all_rows)