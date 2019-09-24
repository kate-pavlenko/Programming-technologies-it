.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	# Ваш код тут
	@apt install python3.7
	@apt install python-pip
	@pip install pipenv
	@pipenv --python 3.7
	@pipenv install requests
	@pipenv install ntplib
	@pipenv install pytest

test:
	@echo "Start tests."
	# Ваш код тут
	@pipenv run pytest tests.py | tee results.txt

run:
	@echo "Run Python app."
	# Ваш код тут
	@pipenv run python app.py | tee -a results.txt

deploy:
	@echo "Adding and Committing results.txt to git."
	# Ваш код тут
	@git add results.txt
	@git commit -m "Ayto push file"
	@git push origin master