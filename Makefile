PYTHON3 = python3
ENVFILE = env/devenv.sh
ENVFILE-TEST = env/devenv-test.sh

run:
	@source $(ENVFILE); $(PYTHON3) run-server.py

run-test:
	@source $(ENVFILE-TEST); $(PYTHON3) run-server.py

test:
	@source $(ENVFILE-TEST); $(PYTHON3) dotest.py

cui-client:
	@$(PYTHON3) run-cuiclient.py
