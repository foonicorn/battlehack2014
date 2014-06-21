.PHONY: tests alltests coverage coverage-html allcoverage allcoverage-html devinstall tox docs clean pyi18n jsi18n
APP=src/
COV=battlehack
OPTS=

help:
	@echo "tests - run tests"
	@echo "coverage - run tests with coverage enabled"
	@echo "coverage-html - run tests with coverage html export enabled"
	@echo "devinstall - install all packages required for development"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "clean - Clean build related files"
	@echo "pyi18n - generate and compile i18n related python files"
	@echo "jsi18n - generate and compile i18n related js files"



tests:
	py.test ${OPTS} ${APP}


coverage:
	py.test --cov=${COV} --cov-report=term-missing ${OPTS} ${APP}


coverage-html:
	py.test --cov=${COV} --cov-report=html ${OPTS} ${APP}


devinstall:
	npm install
	pip install -e .
	pip install -r resources/requirements-develop.txt


tox:
	tox -c src/tox.ini


docs: clean
	sphinx-apidoc --force -o docs/modules/ src/battlehack src/battlehack/*/migrations
	$(MAKE) -C docs clean
	$(MAKE) -C docs html


clean:
	rm -fr build/ src/build
	rm -fr dist/ src/dist
	rm -fr *.egg-info src/*.egg-info
	rm -fr htmlcov/
	$(MAKE) -C docs clean


pyi18n:
	python src/manage.py babel makemessages -d django -l de
	python src/manage.py babel compilemessages -d django -l de

jsi18n:
	python src/manage.py babel makemessages -d djangojs -l de
	python src/manage.py babel compilemessages -d djangojs -l de
	python src/manage.py compilejsi18n -d djangojs -l de
