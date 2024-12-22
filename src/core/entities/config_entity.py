import os

from dataclasses import dataclass
from typing import Optional, Dict, List

from src.core.constants import CloneRepoConstants
from src.core.constants import AnalyzeRepoConstants


# Clone Repository Configuration Entities
cnc = CloneRepoConstants()
@dataclass
class RepositoryConfig:
    """
    Data class to hold repository configuration.
    """
    repo_url: str
    repo_path: str = None  # Updated to None, to be dynamically generated
    branch: str = cnc.BRANCH  # Default branch to clone

    def __post_init__(self):
        # Automatically construct the full path using the repo name
        repo_name = os.path.basename(self.repo_url.rstrip('/').replace('.git', ''))
        self.repo_path = os.path.join(cnc.DATA_DIR, cnc.REPOSITORY_DIR, repo_name)
