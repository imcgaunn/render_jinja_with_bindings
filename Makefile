.SHELL := /bin/bash
.DEFAULT_GOAL := help

.PHONY : help
help :
	@echo "'make help' to print this help message"
	@echo "'make fmt' to run formatter on codebase"
	@echo "'make test' to run unit tests with pytest"

.PHONY : test
test :
	poetry run pytest -s tests/

.PHONY : fmt
fmt :
	poetry run black .
