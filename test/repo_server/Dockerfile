FROM python:3.11-slim
WORKDIR /app

COPY ./repo_server/Auth.py /app/repo_server/Auth.py
COPY ./repo_server/config.json /app/repo_server/config.json
COPY ./repo_server/Config.py /app/repo_server/Config.py
COPY ./repo_server/FileSystem.py /app/repo_server/FileSystem.py
COPY ./repo_server/main.py /app/repo_server/main.py
COPY ./repo_server/pyproject.toml /app/repo_server/pyproject.toml
WORKDIR /app/repo_server

RUN python -m pip install --upgrade pip
RUN python -m pip install poetry pytest-depends
RUN python -m poetry install

RUN python -m poetry run flask --app main set-path /share