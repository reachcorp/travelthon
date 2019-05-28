rm -rf ./docker/context/dockerdist/*
cp -Rf ./README.md ./docker/context/dockerdist/
mkdir -p ./docker/context/dockerdist/src/ && cp -Rf ./src/* ./docker/context/dockerdist/src/
cp -Rf ./travelthon.iml ./docker/context/dockerdist/
cp -Rf ./travelthon.py ./docker/context/dockerdist/
cp -Rf ./entrypoint.sh ./docker/context/dockerdist/
cp -Rf ./requirements.txt ./docker/context/dockerdist/

docker-compose -f ./docker/travelthon.yml build
