docker build . -t binancepostgres
docker run --rm -P -d --name binancepostgres binancepostgres
# split these commands into separate shell files
docker exec -it binancepostgres psql -U username database