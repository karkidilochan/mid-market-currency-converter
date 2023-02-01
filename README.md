# Mid-market Currency Converter

This repository contains the code for the API that converts mid-market currencies for given source and target currencies. It scrapes the exchange rates from wise.com and calculates the converted amount to provide a response.

## Project Setup

The project is **containerized using docker** to ensure consistent dev environment across developers and create a "good-enough" replica of the production environment.
The project uses requirement.txt for packaging and dependency management. It is also used to create a **virtual environment** from the dependencies listed in the file.

The developer is expected to install the following tools before starting work on this project:

- `Docker`
- `git`
- `python 3.11.0a3`
- `make`\*\*

**\*Why is `make` a pre-requisite?**
`Makefile` is used to help with some commands that are frequently used in the development worflow like:

- Setting up virtual environment
- Building docker images
- Installing requirements

## Setup virtual environment

In order to maintain a consistent development environment across all developers, it is advised that they install [Pyenv](https://github.com/pyenv/pyenv) which is a **Python Version Management** tool. This allows to download and switch between multiple versions of python easily. This project uses Python 3.11.0a3 as specified in the .python-version file.

## Build Docker Images

First build the backend docker image using the following make command:

```sh
make docker/build
```

## Collect Environment file

Refer to the "dev.env" file and collect all the required environment variables to run the containers.

## Run the containers

Use the following make command to run the docker container:

```sh
make docker/run
```

The api docs should be accessible at localhost:5000/api/docs.

## Running DB Migrations

I am using PostgreSQL as the database of choice to store/fetch data in the pipeline. So, naturally, you will need to create and run migrations to change the table schemas in database. `alembic` is used to handle migrations in this project which under the hood uses `SQLAlchemy` engine to connect to the database.

Following is the common sequence of actions you would perform to create & run migrations in the database during local development.

- Add/Remove or Make changes to the table schemas in `src/db/models` folder. Use `SQLAlchemy ORM` to define the models.

- Attach a shell to the docker container

  ```
  docker exec -it <container-id> sh
  ```

- Once inside the container, `cd src/db` to get into the directory that contains the `alembic.ini` file

- Here, you can run `alembic` commands to auto-generate the migration

  ```
  alembic revision --autogenerate -m "<migration name>"
  ```

- This will create a migration file that has upgrade and downgrade commands. Check it thoroughly.

- Run migrations

  ```
  alembic upgrade head
  ```

  Pending migrations are automatically applied when you spin up the container next time after closing/exiting.

## Pre-commit checks

To ensure strict linting in the future commits, I encourage using a pre-commit hook:

## 1. Setup the pre-commit hook

- Setup virtualenv

```sh
make venv/build
```

- Install precommit in the venv

```sh
pre-commit install
```

- Now the pre-commit hook should run before each commit. Or, you can check by using:

```sh
pre-commit run --all-files
```
