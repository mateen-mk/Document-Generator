import os

from dataclasses import dataclass
from typing import Optional, Dict, List

from src.core.constants import CloneRepoConstants
from src.core.constants import AnalyzeRepoConstants



# Clone Repository Configuration Entities
cnc = CloneRepoConstants()
@dataclass
class CloneRepoConfig:
    """
    Data class to hold repository configuration.
    """
    repo_url: str
    branch: str = cnc.BRANCH  # Default branch to clone

    def __post_init__(self):
        # Automatically construct the repo_name and repo_path based on the repo_url
        self.repo_name = os.path.basename(self.repo_url.rstrip('/').replace('.git', ''))
        self.repo_path = os.path.join(cnc.DATA_DIR, cnc.REPOSITORY_DIR, self.repo_name)



# Anlyze Repository Configuration entities
arc = AnalyzeRepoConstants()
@dataclass
class AnalyzeRepoConfig:
    """
    Configuration for analyzing a cloned repository.
    """
    repo_path: str  # Path to the cloned repository
    file_extensions: Optional[Dict[str, str]] = None  # Custom file extensions for language mapping
    languages: Optional[List[str]] = None  # Custom list of programming languages

    def __post_init__(self):
        """
        Initializes default values if none are provided.
        """
        self.file_extensions = self.file_extensions or arc.DEFAULT_FILE_EXTENSIONS
        self.languages = self.languages or arc.DEFAULT_LANGUAGES

        # Ensure the path exists
        if not os.path.exists(self.repo_path):
            raise FileNotFoundError(arc.MISSING_REPO_PATH.format(self.repo_path))
