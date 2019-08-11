PYTHON3 = python3
PROCESSING = processing-java
ENVFILE = env/devenv.sh
ENVFILE-TEST = env/devenv-test.sh
MAKEFILE_DIR := $(dir $(lastword $(MAKEFILE_LIST)))

run:
	@source $(ENVFILE); $(PYTHON3) run-server.py

run-test:
	@source $(ENVFILE-TEST); $(PYTHON3) run-server.py

test:
	@source $(ENVFILE-TEST); $(PYTHON3) dotest.py

cui-client:
	@$(PYTHON3) run-cuiclient.py

gui-client:
	@$(PROCESSING) --force --sketch=$(realpath $(MAKEFILE_DIR))/gui_client --run
