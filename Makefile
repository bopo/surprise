# Makefile six

PIP=$(VIRTUAL_ENV)/bin/pip 
PY=$(VIRTUAL_ENV)/bin/python

.PHONY: clean-pyc clean-build docs pack clean clean-others req pep8

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-others - remove Thumbs.db, etc file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "pep8 - check style with pep8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "req - install project requirements"
	@echo "req.update - update project requirements"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "dist - package"
	@echo "install - install the package to the active Python's site-packages"

clean: clean-build clean-others clean-pyc clean-test clean-runtime
distclean: clean-build clean-others clean-pyc clean-test clean-runtime clean-database

clean-database:
	rm -fr database/backups/*
	rm -fr database/fixtrues/*

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -rf '*.tgz'
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.log' -exec rm -f {} +
	find . -name '*.sql' -exec rm -f {} +

clean-others:
	find . -name 'Thumbs.db' -exec rm -f {} \;

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -rf .tox/
	rm -rf .coverage
	rm -rf htmlcov/

clean-runtime:
	rm -fr .runtime/**/**

lint:
	flake8 restful

pack:
	tar zcfv ../backup/server.tgz .

test:
	@$(PY)  manage.py test


tests:
	@$(PY) scripts/runtests.py

test-all:
	tox

coverage:
	coverage run --source vin-delphos setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs:
	rm -f docs/vin-delphos.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ vin-delphos
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html
	
req.all: req.base req.local req.test req.docs req.scrapy

req.base:
	@$(PIP) install  -r requirements/base.txt

req.update:
	@$(PIP) install  -U -r requirements/base.txt

req.prod:
	@$(PIP) install  -U -r requirements/prod.txt

req.test:
	@$(PIP) install  -U -r requirements/test.txt

req.docs:
	@$(PIP) install  -U -r requirements/docs.txt

req.local:
	@$(PIP) install  -U -r requirements/local.txt

req.scrapy:
	@$(PIP) install  -U -r requirements/scrapy.txt

pep8:
	@pep8 --filename="*.py" --ignore=W --first --show-source --statistics --count


release: clean req.prod
	@$(PY) manage.py test


startup: clean req.prod
	@$(PY) manage.py test

dist: clean
	@$(PY) setup.py sdist
	@$(PY) setup.py bdist_wheel
	ls -l dist

shell:
	@$(PY)  manage.py shell_plus

install: clean
	@$(PY)  setup.py install
# DO NOT DELETE
