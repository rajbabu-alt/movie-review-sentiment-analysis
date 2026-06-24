import os
import tarfile
import urllib.request

URL = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

DATA_DIR = "data/raw"
FILE_PATH = os.path.join(DATA_DIR, "aclImdb_v1.tar.gz")

def download():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(FILE_PATH):
        print("Downloading IMDb dataset...")
        urllib.request.urlretrieve(URL, FILE_PATH)
        print("Download complete.")
    else:
        print("Dataset already exists.")

def extract():
    if not os.path.exists(os.path.join(DATA_DIR, "aclImdb")):
        print("Extracting dataset...")
        with tarfile.open(FILE_PATH, "r:gz") as tar:
            tar.extractall(path=DATA_DIR)
        print("Extraction complete.")
    else:
        print("Already extracted.")

if __name__ == "__main__":
    download()
    extract()