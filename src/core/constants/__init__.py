from dataclasses import dataclass


# Clone Repository constants
@dataclass
class CloneRepoConstants:
    """
    Constants used in the cloning process.
    """
    DATA_DIR = 'data'
    REPOSITORY_DIR = 'repository'
    BRANCH = 'main'
    CLONING_FAILED = "Failed to clone repository: {}"
    UNEXPECTED_ERROR = "An unexpected error occurred during the cloning process."


# Analyze Repository constants
@dataclass
class AnalyzeRepoConstants:
    """
    Constants used in the repository analysis process.
    """
    ANALYSIS_SUCCESS = "Repository analysis completed successfully."
    ANALYSIS_ERROR = "An error occurred during repository analysis."
    MISSING_REPO_PATH = "The repository path does not exist: {}"
    NO_FILES_FOUND = "No files found in the repository: {}"
    DEFAULT_LANGUAGES = ['Python', 'JavaScript', 'HTML', 'CSS', 'Markdown', 'YAML', 'JSON', 'Java','Notebook']
    DEFAULT_FILE_EXTENSIONS = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.html': 'HTML',
        '.css': 'CSS',
        '.md': 'Markdown',
        '.yaml': 'YAML',
        '.yml': 'YAML',
        '.json': 'JSON',
        '.java': 'Java',
        '.ipynb':'Notebook',
    }
