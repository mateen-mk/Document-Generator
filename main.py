from src.pipeline.pipeline import RepositoryPipeline

repo_url = input('Enter Github Repository URL: ')

repopipe = RepositoryPipeline(repo_url)
repopipe.run_pipeline()