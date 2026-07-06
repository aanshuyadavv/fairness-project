def save_json_prediction(df, save_path):

    df.to_json(
        save_path,
        orient="records",
        indent=2
    )