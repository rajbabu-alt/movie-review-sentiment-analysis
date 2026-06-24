from pathlib import Path
import pandas as pd


def load_reviews(folder_path, label):
    reviews = []

    for file_path in Path(folder_path).glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        reviews.append({
            "review": text,
            "sentiment": label
        })

    return reviews
