import os
from pathlib import Path


def assets(subdir: str | None = None) -> str:
  ensure_context()
  assets_dir = os.environ["ASSETS_DIR"]
  if subdir:
    assets_dir += f"/{subdir}"
  return assets_dir


def ensure_context() -> None:
    context = detect_context()

    project_root = Path(__file__).resolve().parents[2]
    print(project_root)
    assets_dir = {
        "local": project_root / "src" / "assets",
        "colab": project_root / "src" / "assets",
    }[context]

    if not assets_dir.exists():
        raise FileNotFoundError(f"Could not find assets directory: {assets_dir}")

    os.environ["ASSETS_DIR"] = str(assets_dir)


def detect_context() -> str:
  is_colab = any(env_var.startswith("COLAB_") for env_var in os.environ)
  return "colab" if is_colab else "local"
