import ssl
import urllib.request
import zipfile
from pathlib import Path

PACKAGES = {
    "punkt": "https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt.zip",
    "punkt_tab": "https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt_tab.zip",
    "averaged_perceptron_tagger_eng": "https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/taggers/averaged_perceptron_tagger_eng.zip",
}


def download_and_extract(name: str, url: str, target_dir: Path, download_dir: Path) -> None:
    zip_path = download_dir / f"{name}.zip"
    print(f"Downloading {name}...")

    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=context) as response:
        zip_path.write_bytes(response.read())

    print(f"Extracting {name}...")
    with zipfile.ZipFile(zip_path) as archive:
        archive.extractall(target_dir)


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    nltk_data_dir = project_root / "nltk_data"
    download_dir = project_root / ".cache" / "nltk_downloads"

    tokenizers_dir = nltk_data_dir / "tokenizers"
    taggers_dir = nltk_data_dir / "taggers"
    download_dir.mkdir(parents=True, exist_ok=True)
    tokenizers_dir.mkdir(parents=True, exist_ok=True)
    taggers_dir.mkdir(parents=True, exist_ok=True)

    download_and_extract("punkt", PACKAGES["punkt"], tokenizers_dir, download_dir)
    download_and_extract("punkt_tab", PACKAGES["punkt_tab"], tokenizers_dir, download_dir)
    download_and_extract(
        "averaged_perceptron_tagger_eng",
        PACKAGES["averaged_perceptron_tagger_eng"],
        taggers_dir,
        download_dir,
    )

    print("NLTK data is ready.")


if __name__ == "__main__":
    main()

