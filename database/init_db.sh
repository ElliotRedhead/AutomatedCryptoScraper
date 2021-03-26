docker build . -t binancepostgres &&
docker run --rm -P -d -p 5432:5432 --name binancepostgres binancepostgres