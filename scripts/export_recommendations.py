import json
import pandas as pd
import torch

from recbole.quick_start import load_data_and_model
from recbole.data.interaction import Interaction


# MODEL_PATH = "saved\BPR-Jun-26-2026_18-59-53.pth"
MODEL_PATH = "saved\Pop-Jun-27-2026_21-42-27.pth"

# Load trained model
config, model, dataset, train_data, valid_data, test_data = load_data_and_model(
    model_file=MODEL_PATH
)

model.eval()

TOP_K = 10

all_rows = []

# loop through users
for user_id in range(1, dataset.user_num):

    interaction = Interaction({
        'user_id': torch.tensor([user_id])
    })

    scores = model.full_sort_predict(interaction)

    top_scores, top_items = torch.topk(scores, TOP_K)

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

# Create DataFrame
df = pd.DataFrame(all_rows)

print(df.head())

# Save JSON
df.to_json(
    "fairness_project/outputs/pop/recommendations.json",
    orient="records",
    indent=2
)

print("\nRecommendations exported successfully!")