from recbole.quick_start import load_data_and_model

from extract_recommendations import extract_recommendations_recbole
from save_json import save_json_prediction


MODEL_PATH = "saved/Pop-Jun-27-2026_21-42-27.pth"

config, model, dataset, train_data, valid_data, test_data = load_data_and_model(
    model_file=MODEL_PATH
)

df = extract_recommendations_recbole(
    model,
    dataset,
    top_k=10
)

save_json_prediction(
    df,
    "fairness_project/outputs/pop/recommendations.json"
)

print(df.head())
print("\nRecommendations exported successfully!")