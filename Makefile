install:
	pip install -r requirements.txt

lint:
	pylint accounts app cars

prettier:
	isort .
	blue .

test:
	pytest . -v

pre-commit:
	pre-commit run --all-files