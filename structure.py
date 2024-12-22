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

# Create directories and files
def create_folder_structure():
    """
    Creates the folder structure and files for the project.
    """
    for filepath in list_of_files:
        filepath = Path(filepath)
        if filepath.suffix == "":  # If it's a directory
            os.makedirs(filepath, exist_ok=True)
        else:  # If it's a file
            filedir, filename = os.path.split(filepath)
            if filedir:
                os.makedirs(filedir, exist_ok=True)
            if not os.path.exists(filepath):
                with open(filepath, "w") as f:
                    pass

if __name__ == "__main__":
    create_folder_structure()
    print("Folder structure and files created successfully!")
