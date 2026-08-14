import importlib
import platform
import sys

PACKAGES = [
    "numpy",
    "pandas",
    "sklearn",
    "torch",
    "tensorflow",
    "transformers",
    "datasets",
    "kss",
    "konlpy",
    "kiwipiepy",
    "langchain",
    "faiss",
    "chromadb",
]


def main() -> None:
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print(f"Machine: {platform.machine()}")

    missing = []
    for package in PACKAGES:
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "installed")
            print(f"{package}: {version}")
        except Exception as exc:  # noqa: BLE001
            missing.append((package, exc))
            print(f"{package}: NOT AVAILABLE ({exc})")

    if "torch" not in {name for name, _ in missing}:
        import torch

        print(f"torch.backends.mps.built: {torch.backends.mps.is_built()}")
        print(f"torch.backends.mps.available: {torch.backends.mps.is_available()}")

    if missing:
        names = ", ".join(name for name, _ in missing)
        raise SystemExit(f"Missing packages: {names}")

    print("Environment check passed.")


if __name__ == "__main__":
    main()
