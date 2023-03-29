FROM python:3.11-slim
WORKDIR /app

RUN apt-get update -y
RUN apt-get install qemu-system-x86 qemu-system-aarch64 debootstrap libguestfs-tools -y

COPY ./container_manager/src /app/container_manager/src
COPY ./container_manager/scripts /app/container_manager/scripts
COPY ./container_manager/pyproject.toml /app/container_manager/pyproject.toml
COPY ./container_manager/run.py /app/container_manager/run.py
COPY ./container_manager/server.py /app/container_manager/server.py
COPY ./container_manager/README.md /app/container_manager/README.md
COPY ./test/pytest /app/container_manager/test
WORKDIR /app/container_manager

RUN python -m pip install --upgrade pip
RUN python -m pip install poetry pytest-depends
RUN python -m poetry install

RUN mkdir /root/.containers
RUN touch /root/.containers/server.log