from pathlib import Path

def generate_readme():
    Path("README.md").write_text("# My Project\n")

def generate_license():
    Path("LICENSE").write_text("MIT License")

def generate_gitignore():
    Path(".gitignore").write_text("__pycache__/")
