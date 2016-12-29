.PHONY: help
help:
	@echo "  env         create a development environment using virtualenv"
	@echo "  deps        install dependencies using pip"
	@echo "  clean       remove unwanted files like .pyc's"
	@echo "  lint        check style with flake8"
	@echo "  test        run all your tests using py.test"

.PHONE: deps
deps:
	pip install -r requirements.txt

.PHONY: clean
clean:
	python manage.py clean

.PHONY: lint
lint:
	flake8 .

.PHONY: test
test:
	py.test

.PHONY: freeze
freeze:
	pip freeze > requirements.txt
