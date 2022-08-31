.PHONY: runpostgres rundjango

runpostgres:
	docker run --name hexpostgres -p 5432:5432 -e POSTGRES_USER=octane -e POSTGRES_DB=octane -e POSTGRES_PASSWORD=octane -d postgres:14.5-alpine

rundjango:
	python manage.py runserver
