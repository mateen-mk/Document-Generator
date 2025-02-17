import os
from pathlib import Path

# Define the list of files
list_of_files = [
    "data/repository/.gitkeep",  # To store cloned repository files
    "data/generated_docs/.gitkeep",  # To store generated documentation files

    "models/llama3/.gitkeep",  # Directory for Llama 3 model and configurations

    "src/__init__.py",  # Marks the directory as a Python package
    "src/clone_repo.py",  # Script to clone and fetch GitHub repository
    "src/analyze_repo.py",  # Script to analyze files and extract metadata
    "src/doc_generator.py",  # Script to generate human-like documentation
    "src/app.py",  # Frontend application script (Streamlit/Flask)

    "tests/test_analyze.py",  # Unit tests for repository analysis
    "tests/test_doc_gen.py",  # Unit tests for document generation

    "requirements.txt",  # Python dependencies
    "README.md",  # Project documentation
    "config.yaml",  # Configuration file
]


def create_folder_structure():
    # Create directories and files
    for filepath in list_of_files:
        if filepath.endswith("/"):  # Check if it's a directory
            os.makedirs(filepath, exist_ok=True)
        else:  # It's a file
            filepath = Path(filepath)
            filedir = filepath.parent
            if filedir:  # Ensure parent directory exists
                os.makedirs(filedir, exist_ok=True)
            if not filepath.exists():  # Create the file if it doesn't exist
                filepath.touch()

if __name__ == '__main__': 
    create_folder_structure()
    print("Folder structure created successfully.")
