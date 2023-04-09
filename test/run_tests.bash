#!/bin/bash

test_scripts=()
all_test_scripts=()
all_test_scripts+=("test_help")
all_test_scripts+=("test_run")
all_test_scripts+=("test_put_get")
all_test_scripts+=("test_ct")
#all_test_scripts+=("test_many")
#all_test_scripts+=("test_upload_download")
#all_test_scripts+=("test_build")

for var in "$@"
do
    test_scripts+=( $var )
done
if (( ! ${#test_scripts[@]} )); then
    test_scripts=( "${all_test_scripts[@]}" )
    test_scripts+=($all_test_scripts)
fi

test_script_str=""
for script in "${test_scripts[@]}"
do
    test_script_str+="test/$script.py "
done

docker network create Jabberwocky

docker compose -f ./container_manager/docker-compose.yml build
docker compose -f ./repo_server/docker-compose.yml build

docker compose -f ./container_manager/docker-compose.yml up -d --remove-orphans
docker compose -f ./repo_server/docker-compose.yml up -d --remove-orphans

docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' repo_server > repo_server.ip
docker cp repo_server.ip container_manager:/share/repo_server.ip
rm -f repo_server.ip

docker exec -it container_manager python -m poetry run pytest $test_script_str

docker compose -f ./container_manager/docker-compose.yml down
docker compose -f ./repo_server/docker-compose.yml down