DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

if [ "$(docker ps -q -f name=binancepostgres)" ]; then
	# cleanup old container
	while true; do
		echo "A binancepostgres container already exists, this process will overwrite the previous container."
		read -p "Do you wish to proceed? (y/n) " yn
		# select yn in "Yes" "No"; do
		case $yn in
			[Yy]* ) docker stop binancepostgres && docker build $DIR -t binancepostgres && docker run --rm -P -d -p 5432:5432 --name binancepostgres binancepostgres; break;;
			[Nn]* ) exit;;
			* ) echo "Please answer y/yes or n/no. "
		esac
	done
	else
		docker build $DIR -t binancepostgres &&
		docker run --rm -P -d -p 5432:5432 --name binancepostgres binancepostgres
fi
