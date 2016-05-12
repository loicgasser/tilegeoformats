VENV = .venv
PYTHON_CMD = $(VENV)/bin/python

.PHONY: help
help:
	@echo "Usage: make <target>"
	@echo
	@echo "Possible targets:"
	@echo
	@echo "- all            Install the app"
	@echo "- clean          Clean all generated files and folders"
	@echo

.PHONY: all
all:
	@if [ ! -d $(VENV) ]; \
	then \
		virtualenv $(VENV) --distribute; \
	fi; \
	$(PYTHON_CMD) setup.py develop
	npm install

.PHONY: clean
clean:
	rm -rf $(VENV)
	rm -rf *.egg-info
	rm -rf node_modules
