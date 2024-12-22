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


