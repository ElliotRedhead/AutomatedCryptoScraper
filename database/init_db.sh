DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

if [ "$(docker ps -q -f name=binancepostgres)" ]; then
	# cleanup old container
    docker stop binancepostgres
fi

docker build $DIR -t binancepostgres &&
docker run --rm -P -d -p 5432:5432 --name binancepostgres binancepostgres