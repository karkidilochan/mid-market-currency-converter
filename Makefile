venv/build:
	python3 -m venv virtualenv
	virtualenv/bin/python -m pip install -r requirements.txt

venv/activate:
	source virtualenv/bin/activate

docker/build:
	docker build -t currency-converter-backend -f Dockerfile .

docker/build-and-run:
	docker build -t currency-converter-backend -f Dockerfile .
	docker-compose up --build

docker/run:
	docker-compose up
