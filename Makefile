#.ONESHELL:

#.PHONY: install


classify:
	. env/bin/activate; python3 classifer.py

tree: clean
	. env/bin/activate; python3 train_tree.py

forest: clean
	. env/bin/activate; python3 train_forest.py

clean:
	- rm data/model/* 2> /dev/null
	clear

build:
	docker build -t decision:x86_64 .

image_save: build
	docker save decision:x86_64 > decision_x86_64.tar

image_import:
	docker load < decision_x86_64.tar

docker_hub: build
	docker tag decision:x86_64 jorgensenj/decision:x86_64
	docker push jorgensenj/decision:x86_64


docker_buildx:
	docker buildx use mybuilder
	docker buildx build --platform linux/amd64,linux/arm64 -t jorgensenj/decision:latest --push .