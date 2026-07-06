from scripts.convert_recbole import (
    extract_recommendations_recbole,
    get_number_of_items,
    get_number_of_users
)

from metrics.coverage import coverage

from utils import save_json_prediction


MODEL_PATH = "saved/Pop-Jun-27-2026_21-42-27.pth"


df, dataset = extract_recommendations_recbole(
    MODEL_PATH,
    top_k=10
)


total_users = get_number_of_users(dataset)

total_items = get_number_of_items(dataset)


print("Total users:", total_users)

print("Total items:", total_items)


unique_items, coverage_score = coverage(
    df,
    total_items
)


print("Unique recommended items:", unique_items)

print("Coverage:", coverage_score)


save_json_prediction(
    df,
    "fairness_project/outputs/pop/recommendations.json"
)


print("JSON file saved successfully")