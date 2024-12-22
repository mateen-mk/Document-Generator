from git import Repo, GitCommandError
from src.core.logger import get_logger
from src.core.exception import DocGenException
from src.core.constants import CloneRepoConstants
from src.core.entities.config_entity import RepositoryConfig
import os


class RepositoryCloner:
    """
    A class to encapsulate repository cloning logic.
    """

    def __init__(self, repo_config: RepositoryConfig):
        """
        Initializes the RepositoryCloner with a RepositoryConfig object.
        :param repo_config: RepositoryConfig containing the repository details.
        """
        self.repo_config = repo_config
        self.logger = get_logger("clone_repo")
        self.repo_name = self._extract_repo_name()

    def clone(self):
        """
        Clones the GitHub repository to the local directory specified in the repo_config.
        """
        try:
            self._validate_target_directory()

            if self._is_already_cloned():
                self.logger.info(f"Repository already exists at {self.repo_config.repo_path}. Skipping clone.")
                return

            self.logger.info(f"Cloning repository from {self.repo_config.repo_url} to {self.repo_config.repo_path}...")
            Repo.clone_from(
                self.repo_config.repo_url, self.repo_config.repo_path, branch=self.repo_config.branch
            )
            self.logger.info("Repository successfully cloned.")

        except GitCommandError as e:
            self.logger.error(f"Error during cloning: {str(e)}")
            raise DocGenException(CloneRepoConstants.CLONING_FAILED.format(self.repo_config.repo_url)) from e

        except Exception as e:
            self.logger.error(f"Unexpected error: {str(e)}")
            raise DocGenException(CloneRepoConstants.UNEXPECTED_ERROR) from e

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

    def _extract_repo_name(self):
        """
        Extracts the repository name from the repository URL.
        :return: Repository name as a string.
        """
        repo_name = os.path.basename(self.repo_config.repo_url.rstrip('/').replace('.git', ''))
        return repo_name
