from dataclasses import dataclass
from typing import Dict, List

# Repository Analysis artifact
@dataclass
class AnalyzeArtifact:
    """
    A data class to store the results of repository analysis.
    """
    structure: Dict[str, List[str]]  # Directory structure
    file_summary: List[str]         # List of all files with relative paths
    metadata: Dict[str, any]        # Metadata such as total files, directories, and languages
