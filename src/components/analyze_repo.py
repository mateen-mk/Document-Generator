import os
import sys
from typing import Dict, List

from src.core.logger import logging
from src.core.exception import DocGenException
from src.core.constants import AnalyzeRepoConstants
from src.core.entities.config_entity import AnalyzeRepoConfig
from src.core.entities.artifact_entity import AnalyzeRepoArtifact


class RepositoryAnalyzer:
    """
    A class to analyze a cloned repository and extract useful metadata.
    """

    def __init__(self, analyze_config: AnalyzeRepoConfig):
        """
        Initializes the RepositoryAnalyzer with an AnalyzeRepoConfig object.
        :param analyze_config: AnalyzeRepoConfig containing analysis configuration.
        """
        self.analyze_config = analyze_config

    def analyze(self) -> AnalyzeRepoArtifact:
        """
        Analyzes the repository structure and content.
        :return: A AnalyzeArtifact object containing metadata about the repository.
        """
        try:
            logging.info(f"Starting analysis for repository at {self.analyze_config.repo_path}")

            if not os.path.exists(self.analyze_config.repo_path):
                raise DocGenException(AnalyzeRepoConstants.MISSING_REPO_PATH.format(self.analyze_config.repo_path), sys)

            structure = self._get_structure()
            file_summary = self._summarize_files(structure)
            metadata = {
                "total_files": len(file_summary),
                "total_directories": len(structure),
                "languages": self._get_languages(file_summary),
            }

            logging.info(AnalyzeRepoConstants.ANALYSIS_SUCCESS)
            return AnalyzeRepoArtifact(structure=structure, file_summary=file_summary, metadata=metadata)

        except Exception as e:
            logging.error(f"{AnalyzeRepoConstants.ANALYSIS_ERROR}: {str(e)}")
            raise DocGenException(e, sys)

    def _get_structure(self) -> Dict[str, List[str]]:
        """
        Retrieves the folder structure of the repository.
        :return: A dictionary with directories as keys and files as values.
        """
        structure = {}
        for root, dirs, files in os.walk(self.analyze_config.repo_path):
            relative_path = os.path.relpath(root, self.analyze_config.repo_path)
            structure[relative_path] = files
        return structure

    def _summarize_files(self, structure: Dict[str, List[str]]) -> List[str]:
        """
        Summarizes all files in the repository.
        :param structure: The folder structure of the repository.
        :return: A list of all files with their relative paths.
        """
        return [
            os.path.join(directory, file)
            for directory, files in structure.items()
            for file in files
        ]

    def _get_languages(self, files: List[str]) -> List[str]:
        """
        Identifies programming languages based on file extensions.
        :param files: List of files in the repository.
        :return: A list of detected programming languages.
        """
        detected_languages = set()
        for file in files:
            _, ext = os.path.splitext(file)
            if ext in self.analyze_config.file_extensions:
                detected_languages.add(self.analyze_config.file_extensions[ext])
        return list(detected_languages)
