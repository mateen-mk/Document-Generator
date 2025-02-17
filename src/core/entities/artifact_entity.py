from dataclasses import dataclass
from typing import Dict, List


# Clone Repository artifact
@dataclass
class CloneRepoArtifact:
    repo_name: str
    repo_path: str


# Repository Analysis artifact
@dataclass
class AnalyzeRepoArtifact:
    structure: Dict[str, List[str]]  # Directory structure
    file_summary: List[str]         # List of all files with relative paths
    metadata: Dict[str, any]        # Metadata such as total files, directories, and languages
