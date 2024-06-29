setupenv:
	@virtualenv .venv
	@pip install -r requirements

push:
	@echo "Pushing PR to origin"

test:
	@echo "Testing code"

deploy:
	@echo "Deploying code"

run:
	@echo "Run Proximity Pulse"