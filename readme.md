# Tic-tac-toe REST 

This is a simple FastAPI microservice application written in Python and uses Beanie for MongoDB and pydantic for data validation.

## Getting Started

Pre-requisites:

- Python 3.10 or later
- Docker and Docker Compose

## Installation

```shell
docker-compose up
```

The application will then be available at `localhost:3001`.

This a FastAPI application, you can access the OpenAPI at `localhost:3001/docs` and interact with the service.

All the data will be stored in a MongoDB database.

## Testing

Tests are written using pytest. Its recommended to create a virtual environemtn to wrap all the requirements, to create one:

```shell
python3.10 -m venv venv
```

to activate it:
```bash
source venv/bin/activate
```

to install the requirements:
```bash
pip install -r requirements.txt
```

To start tests, simply execute:

```shell
python -m unittest discover -s tests
```