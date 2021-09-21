SHELL := /bin/bash

manage_py := python app/manage.py


runserver:
	$(manage_py) runserver 127.0.0.1:8000

migrate:
	$(manage_py) migrate

make_migrations:
	$(manage_py) makemigrations

celery_worker:
	$cd currency_app && celery -A tasks worker --loglevel=INFO

shell:
	$(manage_py) shell_plus --print-sql

worker:
	cd app/currency_app && celery-A settings worker-l info--autoscale=10.0
#cd app && celery-A settings worker-L info-concurrency 20
beat: cd app/currency_app && celery A settings beat-L info

flake8:
	$(manage_py) flake8_check

#Use make 'command_name'  to run it in terminal