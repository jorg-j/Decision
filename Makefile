#.ONESHELL:

#.PHONY: install


classify:
	. env/bin/activate; python3 classifer.py


train:
	. env/bin/activate; python3 train.py
