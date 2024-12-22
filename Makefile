# include .env


# Define the virtual environment directory
VENV_DIR = .docgenenv


# Create the virtual environment
.PHONY: create-venv
create-venv: 
	python -m venv $(VENV_DIR)
	@echo "$(VENV_DIR) has been created."


# Install the requirements of the project
.PHONY: install-requirements
install-requirements: $(VENV_DIR)
	pip install -r requirements.txt
	@echo "Requirements have been installed."


# Update requirements.txt with current environment packages
.PHONY: update-requirements
update-requirements: $(VENV_DIR)
	pip freeze > requirements.txt
	@echo "requirements.txt updated."


# git related
.PHONY: git-push
git-push:
	git add .
	git commit -m "$(msg)"
	git push origin main
