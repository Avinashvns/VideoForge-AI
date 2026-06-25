from pathlib import Path

# Project Root
ROOT = Path(".")

# Folders
folders = [
    "app/audio",
    "app/speech",
    "app/script",
    "app/timeline",
    "app/subtitles",
    "app/images",
    "app/effects",
    "app/renderer",
    "app/config",
    "app/utils",

    "assets/voice",
    "assets/images",
    "assets/music",
    "assets/fonts",

    "output",
    "tests",
    "logs",
    "temp",
    "docs",
]

# Files
files = [
    "requirements.txt",
    "README.md",
    ".gitignore",
    "main.py",
]

# Create folders
for folder in folders:
    path = ROOT / folder
    path.mkdir(parents=True, exist_ok=True)

    # __init__.py inside app folders
    if folder.startswith("app"):
        init_file = path / "__init__.py"
        init_file.touch(exist_ok=True)

# Create files
for file in files:
    (ROOT / file).touch(exist_ok=True)

print("=" * 50)
print("✅ VideoForge-AI Project Structure Created")
print("=" * 50)