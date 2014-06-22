.PHONY: tests alltests coverage coverage-html allcoverage allcoverage-html
APP=src/
COV=battlehack
OPTS=

help:
	@echo "tests - run tests"
	@echo "coverage - run tests with coverage enabled"
	@echo "coverage-html - run tests with coverage html export enabled"


tests:
	py.test ${OPTS} ${APP}


coverage:
	py.test --cov=${COV} --cov-report=term-missing ${OPTS} ${APP}


coverage-html:
	py.test --cov=${COV} --cov-report=html ${OPTS} ${APP}
