include ./.make/colors.mk

NAME = GameStateManager
VERSION = $(shell cat version.txt)
OS = $(shell uname -s)

## —— Help ————————————————————————————————————
help: ## Show help
	@grep -E '(^[a-zA-Z0-9_-]+:.*?##.*$$)|(^##)' Makefile | awk 'BEGIN {FS = ":.*?## "}{printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

## —— Tests ———————————————————————————————————
tests: ## Run tests
	python test.py

## —— Development —————————————————————————————
clean: ## Clean all artefacts: build, venv
	@echo "Cleaning up distutils stuff"
	rm -rf dist
	rm -rf build
	rm -rf ./GameStateMachine.egg-info/
	@echo "Cleaning up byte compiled python stuff"
	find . -maxdepth 1 -type d -name "__pycache__" -exec rm -rv {} +
	@echo "Cleaning venv"
	rm -rf venv
	find -iname "*.pyc" -delete
	@echo "Please run 'deactivate' to deactivate python virtual environment"

version: ## Display the package version
	@echo $(VERSION)

pip-upgrade: ## Upgrades local pip
	. venv/bin/activate; python -m pip install --upgrade pip

venv-test: ## Checks if venv is setup or install virtualenv
	test -d venv || virtualenv venv || pip install virtualenv

venv/touchfile: requirements.txt
venv/touchfile: venv-test
venv/touchfile: pip-upgrade
	. venv/bin/activate; pip install -Ur requirements.txt
	@echo "To activate python virtual environment, please run the command '. venv/bin/activate'"
	touch venv/touchfile

venv: venv/touchfile

init: venv ## Initialize virtual environment

## —— Releasing ———————————————————————————————
build: ## Build package
	. venv/bin/activate; python setup.py sdist

install: ## Install package
	. venv/bin/activate; python setup.py install

check-twine:
	@which twine > /dev/null || { @echo "Twine not found. Installing..."; make install-twine; }

install-twine: init
install-twine: ## Install twine for uploading releases to pypi or testpypi
	. venv/bin/activate; python3 -m pip install --upgrade twine

testpypi:
	python -m twine upload --repository testpypi dist/*

pypi:
	python -m twine upload --repository pypi dist/*

release: ## Releases current built package version
release: check-twine pypi
