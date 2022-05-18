# WepAPPdemo
Webappdemo is a demo project used as a POC.

The application itself is configured to run in a python 3.8 environment using the following packages:

    fastapi
    uvicorn[standard]
    sqlalchemy
    strawberry-graphql[fastapi]
    alembic
    psycopg2
    python-dotenv
    black

# Usage
The project is deployed using Docker Desktop via `docker-compose`.
You first need to checkout the project and build and load the docker containers:
```
docker-compose build
docker-compose up
```
Then, stop the containers and execute the following commands to configure the database table using `alembic`:
```
docker-compose run app alembic revision --autogenerate -m "New Migration"
docker-compose run app alembic upgrade head
```
This will complete the configuration of the application.

# Postgress admin
Point your browser to http://localhost:5050 to access the PostgreSQL administration client.

# Interactive graphQL
Point your browser to http://localhost:8000/graphql to access the grapghQL interactive client.