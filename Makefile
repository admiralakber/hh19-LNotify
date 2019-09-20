help:
	@echo "MULtilingual Appointment Notification"
	@echo "====================================="
	@echo "> reqs/git - pulls / updates git submodules"
	@echo "> compose/dev - runs docker-compose for local development, pass args for different commands"
	@echo "> dev/clean - removes files produced by running compose in development"

reqs/git:
	git submodule update --recursive --remote --init

args=config
compose/dev:
	sudo docker-compose -f docker-compose.yml -f docker-compose.override.yml $(args)

dev/clean:
	sudo find . -iname '*__pycache__' | xargs sudo rm -rv
	
args=config
compose/prod:
	sudo docker-compose -f docker-compose.yml -f docker-compose.prod.yml $(args)
