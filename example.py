import pandas as pd

from recbole.quick_start import load_data_and_model

from metrics.coverage import coverage

from scripts.dataset_info import (
    get_number_of_items,
    get_number_of_users,
)

from scripts.save_json import save_json_prediction


MODEL_PATH = "saved/Pop-Jun-27-2026_21-42-27.pth"

# Load trained model and dataset
config, model, dataset, train_data, valid_data, test_data = load_data_and_model(
    model_file=MODEL_PATH
)

# Get dataset information
total_users = get_number_of_users(dataset)
total_items = get_number_of_items(dataset)

print("Total users:", total_users)
print("Total items:", total_items)

# Load recommendations
df = pd.read_json("fairness_project/outputs/pop/recommendations.json")

# Compute coverage
unique_items, coverage_score = coverage(df, total_items)

print("Unique recommended items:", unique_items)
print("Coverage:", coverage_score)

# Save the DataFrame as a JSON file
save_json_prediction(
    df,
    "fairness_project/outputs/test.json"
)

print("JSON file saved successfully")