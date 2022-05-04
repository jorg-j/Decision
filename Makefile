#.ONESHELL:

#.PHONY: install


classify:
	. env/bin/activate; python3 classifer.py


train:
	. env/bin/activate; python3 train.py


service:
	docker build -t decider .
	python3 docker_extras/createFiles.py
	cd docker_extras; docker build -t deciderhook .
	cd docker_extras; docker-compose up -d