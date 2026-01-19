PYTHON_MODULE = receipt_data_extractor.main
PYTHONPATH = src
PYTHON_ARGS = receipts
VENV_DIR = venv

run:
	@echo "Running $(PYTHON_MODULE) with --print..."
	@python3 -m venv $(VENV_DIR)
	@PYTHONPATH=$(PYTHONPATH) python3 -m $(PYTHON_MODULE) $(PYTHON_ARGS) --print
