help:
	@echo "MULtilingual Appointment Notification"
	@echo "====================================="
	@echo "> reqs/git - pulls / updates git submodules"
	@echo "> compose/dev - runs docker-compose for local development, pass args for different commands"
	@echo "> dev/clean - removes files produced by running compose in development"
	@echo "> setup/prod - sets up production environment"
	@echo "> compose/prod - runs docker-compose for production environment, pass args for different commands"

reqs/git:
	git submodule update --recursive --remote --init

setup/prod:
	cd letsencrypt_nginx; make setup/cert domain=culturefluent.thaum.io
	cd letsencrypt_nginx; make setup/cert domain=api.culturefluent.thaum.io


args=config
compose/dev:
	sudo docker-compose -f docker-compose.yml -f docker-compose.override.yml $(args)

dev/clean:
	sudo find . -iname '*__pycache__' | xargs sudo rm -rv
	
args=config
compose/prod:
	sudo docker-compose -f docker-compose.yml -f docker-compose.prod.yml -f letsencrypt_nginx/docker-compose.yml $(args)

