PYTHON3 = python3
ENVFILE = devenv.sh
ENVFILE-TEST = devenv-test.sh

run:
	@source $(ENVFILE); $(PYTHON3) run.py

test:
	@source $(ENVFILE-TEST); $(PYTHON3) dotest.py
