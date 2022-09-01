# Hexagonal Architecture Example in Python

Welcome! Inside this repository you can find a project using 2 different frameworks and a single business logic module. The folder structure is:

- `corebusiness`: contains the business logic layer
- `djangohex`: contains one implementation of the ports. Django handles HTTPs requests and also its ORM is used to access the database.
- `flaskhex`: contains another implementation of the ports. Flask handles HTTPs requests and Psycopg2 is used to access the database.

![](docs/python-hex.png)

In this example, we have 2 different adapters to handle HTTP requests that use the same use case `SubmitApplicationUseCase`. The business logic is the same for both, but the way the HTTP requests are handled and the database access is implemented differs.

One can add more ways to access the business logic, it could be a Command Line Interface (CLI) for example. It is also possible to add other implementation of the repositories using different libraries.

## Running

To run this project, install the requirements using `pip install -r requirements.txt` and then run:

1. PostgreSQL database: `make runpostgres`
2. Migrate database with Django: `make rundjangomigrations`
3. Django server: `make rundjangoserver`
4. Flask server: `make runflaskserver`

After that, you should have 2 HTTP servers running, Django at port 8000 and Flask at port 5000.

## Testing

This example only contains a single endpoint implemented. The endpoint is responsible to submit an application.

To test it, you should submit a POST request with the form-data parameters: `customer_ssn` and `customer_name` to:

- Django: `http://localhost:8000/app/application`
- Flask: `http://localhost:5000/application`


## References

- https://medium.com/sciforce/another-story-about-microservices-hexagonal-architecture-23db93fa52a2
- https://medium.com/codex/clean-architecture-for-dummies-df6561d42c94
- https://github.com/Sairyss/domain-driven-hexagon
