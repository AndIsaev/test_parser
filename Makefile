init db:
	docker-compose exec web /bin/sh  -c "flask --app backend.app db init --directory=backend/migrations"

migrate:
	docker-compose exec web /bin/sh  -c "flask --app backend.app db migrate --directory=backend/migrations"

upgrade:
	docker-compose exec web /bin/sh  -c "flask --app backend.app db upgrade --directory=backend/migrations"
