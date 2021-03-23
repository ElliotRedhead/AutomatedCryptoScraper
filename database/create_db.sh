docker build . -t binancepostgres
docker run --rm -P -d --name binancepostgres binancepostgres
docker exec -it binancepostgres /bin/bash