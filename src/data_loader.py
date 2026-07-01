from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parent.parent

def load_reviews(folder_path, label):
    reviews = []

    for file_path in Path(folder_path).glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        reviews.append({
            "review": text,
            "sentiment": label
        })

    return reviews
def load_train_data():
    train_path = project_root / "data" / "raw" / "aclImdb" / "train"

    pos_path = train_path / "pos"
    neg_path = train_path / "neg"

    positive_reviews = load_reviews(pos_path,1)
    negative_reviews = load_reviews(neg_path,0)
    all_reviews = positive_reviews + negative_reviews
    df = pd.DataFrame(all_reviews)
    return df
if __name__ == "__main__":
    df = load_train_data()

    print(df.head())
    print(df.shape)