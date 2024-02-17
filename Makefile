install:
	pip install -r requirements.txt

lint:
	isort .
	blue .
	pylint accounts app cars

test:
	pytest . -v