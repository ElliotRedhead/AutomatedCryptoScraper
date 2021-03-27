DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
docker build $DIR -t binancepostgres &&
docker run --rm -P -d -p 5432:5432 --name binancepostgres binancepostgres