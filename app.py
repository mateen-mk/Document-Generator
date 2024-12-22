# app script
from src.core.entities.config_entity import RepositoryConfig
from src.components.clone_repo import RepositoryCloner

def main():
    """
    Main function to interact with the user and clone a repository.
    """
    
    # Prompt user for repository URL
    repo_url = input("Enter the GitHub Repository URL: ")
    
    # Use default path and branch from constants
    repo_config = RepositoryConfig(
        repo_url=repo_url
    )
    
    # Clone the repository
    cloner = RepositoryCloner(repo_config)
    cloner.clone()

if __name__ == "__main__":
    main()
