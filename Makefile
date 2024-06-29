setupenv:
	@virtualenv .venv
	@pip install -r requirements

push:
	@echo "Pushing PR to origin"

test:
	@echo "Testing code"

deploy:
	@echo "Deploying code"
	@echo "Push code to host"
	@echo "Push service to host"
	@echo "Restart service"


run:
	@echo "Run Proximity Pulse"