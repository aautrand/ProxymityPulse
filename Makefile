setupenv:
	@virtualenv .venv
	@source .venv/bin/activate
	@pip install -r requirements

push:
	@echo "Pushing PR to origin"

test:
	@echo "Testing code"

deploy:
	# Only run deploy in the host machine
	@echo "Checking we're in the correct host"
	@echo "Deploying "
	@echo "Updating wlan service"
	#sudo cp scripts/wlan_monitor.sh /usr/bin/local/
	@echo "Updating application service"
	#sudo cp proximity_pulse.py /opt/proximity_pulse/


run:
	@echo "Run Proximity Pulse"
	@sudo python proximity_pulse.py
