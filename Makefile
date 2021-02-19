up:
	@docker-compose -f docker/docker-compose.yml up -d
	@docker ps

down:
	@docker-compose -f docker/docker-compose.yml down
