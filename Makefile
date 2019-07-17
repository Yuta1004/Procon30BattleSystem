PYTHON3 = python3
ENVFILE = devenv.sh

make:
	@$(PYTHON3) run.py

test:
	@source $(ENVFILE); $(PYTHON3) dotest.py
