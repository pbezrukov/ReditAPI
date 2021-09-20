
up:
	@docker-compose build
	@docker-compose up -d
	@docker ps

down:
	@docker-compose down
