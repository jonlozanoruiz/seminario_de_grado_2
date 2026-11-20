.PHONY: all prepare validate train test

all: prepare validate train test

prepare:
	python3 src/prepare.py

validate: prepare
	python3 src/validate.py

train: validate
	python3 src/train.py

lstest: train
	pytest src/test_model.py