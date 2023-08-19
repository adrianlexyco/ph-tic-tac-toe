# Dockerfile

# pull the official docker image
FROM python:3.10.8

# set work directory
WORKDIR /app

# set env variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

# COPY .env to workdir
COPY .env .env
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# ENTRYPOINT ["./docker-entrypoint.sh"]
# copy project
COPY . .
