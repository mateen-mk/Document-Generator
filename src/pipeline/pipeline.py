import sys
from src.core.logger import get_logger
from src.core.exception import DocGenException
from src.components.clone_repo import RepositoryCloner
from src.components.analyze_repo import RepositoryAnalyzer
from src.core.entities.config_entity import CloneRepoConfig, AnalyzeRepoConfig
from src.core.entities.artifact_entity import AnalyzeRepoArtifact


class RepositoryPipeline:
    def __init__(self, repo_url):
        self.logger = get_logger("pipeline")

        self.logger.info("* " * 50)
        self.logger.info("- - - - - Starting Repository Pipeline - - - - -")
        self.logger.info("* " * 50)
        
        self.repo_url = repo_url
        self.clone_repo_config = CloneRepoConfig(repo_url=self.repo_url)

    def start_clone_repository(self):
        """
        This method starts the cloning process for the repository.
        """
        try:
            self.logger.info("\n$ Entering start_clone_repository method of RepositoryPipeline class:")
            
            clone_repo = RepositoryCloner(self.clone_repo_config)
            clone_repo.clone()
            
            self.logger.info("- " * 50)
            self.logger.info("- - - Repository Cloned Successfully! - - -")
            self.logger.info("! Exiting start_clone_repository method of RepositoryPipeline class:")
            self.logger.info("_" * 100)
        
        except Exception as e:
            raise DocGenException(e, sys) from e

    def start_analyze_repository(self):
        """
        This method starts the analysis process for the cloned repository.
        """
        try:
            self.logger.info("\n$ Entering start_analyze_repository method of RepositoryPipeline class:")
            
            analyze_config = AnalyzeRepoConfig(repo_path=self.clone_repo_config.repo_path)
            analyze_repo = RepositoryAnalyzer(analyze_config)
            analyze_artifact = analyze_repo.analyze()
            
            self.logger.info("- " * 50)
            self.logger.info("- - - Repository Analysis Completed Successfully! - - -")
            self.logger.info("! Exiting start_analyze_repository method of RepositoryPipeline class:")
            self.logger.info("_" * 100)

            return analyze_artifact
        
        except Exception as e:
            raise DocGenException(e, sys) from e

    def run_pipeline(self):
        """
        This method runs the complete pipeline for repository cloning and analysis.
        """
        try:
            self.start_clone_repository()
            analyze_artifact = self.start_analyze_repository()
            
            self.logger.info("Pipeline executed successfully.")
            return analyze_artifact
        
        except Exception as e:
            raise DocGenException(e, sys) from e