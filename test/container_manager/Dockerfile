FROM python:3.11-slim
WORKDIR /app

COPY ./container_manager/src /app/container_manager/src
COPY ./container_manager/pyproject.toml /app/container_manager/pyproject.toml
COPY ./container_manager/run.py /app/container_manager/run.py
COPY ./container_manager/server.py /app/container_manager/server.py
COPY ./container_manager/README.md /app/container_manager/README.md
COPY ./test/pytest /app/container_manager/test
WORKDIR /app/container_manager

RUN python -m pip install --upgrade pip
RUN python -m pip install poetry pytest-reportlog
RUN python -m poetry install

RUN mkdir /root/.containers
RUN touch /root/.containers/server.log

ENTRYPOINT python -m poetry run pytest ./test