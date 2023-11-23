### Includes ###
include ./.make/colors.mk

### Variables ###
NAME = GameStateManager
VERSION = $(shell cat version.txt)
OS = $(shell uname -s)

#################

.DEFAULT_GOAL := help
.PHONY: help
help:
	@printf "$(BROWN) Project commands:$(NC)\n"
	@printf "$(GREEN)	help\t$(NC)	Display this help message\n"
	@printf "$(GREEN)	all\t$(NC)	Clean, install venv and build the package\n"
	@printf "$(GREEN)	init\t$(NC)	Initialize the package for development\n"
	@printf "$(GREEN)	install\t$(NC)	Install package for testing\n"
	@printf "$(GREEN)	clean\t$(NC)	Clean package from artefacts\n"
	@printf "$(GREEN)	python\t$(NC)	Build the package\n"
	@printf "$(GREEN)	version\t$(NC)	Display the package version\n"

.PHONY: all
all: clean python

pip-upgrade:
	. venv/bin/activate; python -m pip install --upgrade pip

venv-test:
	test -d venv || virtualenv venv

venv: venv/touchfile

venv/touchfile: requirements.txt venv-test pip-upgrade
	. venv/bin/activate; pip install -Ur requirements.txt
	@echo "To activate python virtual environment, please run the command '. venv/bin/activate'"
	touch venv/touchfile

.PHONY: init
init: venv

.PHONY: clean
clean:
	@echo "Cleaning up distutils stuff"
	rm -rf build
	rm -rf ./GameStateMachine.egg-info/
	@echo "Cleaning up byte compiled python stuff"
	find . -maxdepth 1 -type d -name "__pycache__" -delete
	@echo "Cleaning venv"
	rm -rf venv
	find -iname "*.pyc" -delete
	@echo "Please run 'deactivate' to deactivate python virtual environment"

.PHONY: python
python:
	. venv/bin/activate; python setup.py build

.PHONY: install
install:
	. venv/bin/activate; python setup.py install

.PHONY: version
version:
	@echo $(VERSION)
