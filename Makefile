.PHONY: runpostgres rundjangomigrations rundjangoserver runflaskserver

runpostgres:
	docker run --name hexpostgres -p 5432:5432 -e POSTGRES_USER=octane -e POSTGRES_DB=octane -e POSTGRES_PASSWORD=octane -d postgres:14.5-alpine

rundjangomigrations:
	python manage.py migrate

rundjangoserver:
	python manage.py runserver

runflaskserver:
	flask --app flaskhex.app run
