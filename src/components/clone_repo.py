import sys
from git import Repo, GitCommandError

from src.core.logger import logging
from src.core.exception import DocGenException
from src.core.constants import CloneRepoConstants
from src.core.entities.config_entity import CloneRepoConfig
from src.core.entities.artifact_entity import CloneRepoArtifact



class RepositoryCloner:
    """
    A class to encapsulate repository cloning logic.
    """

    def __init__(self, repo_config: CloneRepoConfig):
        """
        Initializes the RepositoryCloner with a CloneRepoConfig object.
        :param repo_config: CloneRepoConfig containing the repository details.
        """
        self.repo_config = repo_config


    def _validate_target_directory(self):
        """
        Ensures the target directory exists.
        """
        from pathlib import Path
        Path(self.repo_config.repo_path).mkdir(parents=True, exist_ok=True)


    def _is_already_cloned(self):
        """
        Checks if the repository is already cloned by verifying the directory's contents.
        :return: True if already cloned, False otherwise.
        """
        from os import listdir
        return bool(listdir(self.repo_config.repo_path))


    def clone(self):
        """
        Clones the GitHub repository to the local directory specified in the repo_config.
        """
        try:
            self._validate_target_directory()

            if self._is_already_cloned():
                logging.info(f"Repository already exists at {self.repo_config.repo_path}. Skipping clone.")
                return

            # Clone the repository
            logging.info(f"Cloning repository from {self.repo_config.repo_url} to {self.repo_config.repo_path}...")
            Repo.clone_from(self.repo_config.repo_url, self.repo_config.repo_path, branch=self.repo_config.branch)
            logging.info("Repository successfully cloned.")

            # Create and return the CloneRepoArtifact
            clone_repo_artifact = CloneRepoArtifact(self.repo_config.repo_name, self.repo_config.repo_path)
            
            return clone_repo_artifact

        except GitCommandError as e:
            logging.error(f"Error during cloning: {str(e)}")
            raise DocGenException(CloneRepoConstants.CLONING_FAILED.format(self.repo_config.repo_url), sys) from e

        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            raise DocGenException(CloneRepoConstants.UNEXPECTED_ERROR, sys) from e

