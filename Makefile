#.ONESHELL:

#.PHONY: install


classify:
	. env/bin/activate; python3 classifier.py


train:
	. env/bin/activate; python3 train.py

docker-train:
	docker-compose up

service:
	docker build -t decider .
	python3 docker_extras/createFiles.py
	cd docker_extras; docker build -t deciderhook .
	cd docker_extras; docker-compose up -d