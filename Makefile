MIGRATION_NAME ?= ''


run:
	python manage.py runserver
migrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate
migrations-appointments:
	python manage.py makemigrations appointments
migrate-appointments:
	python manage.py migrate appointments
superuser:
	python manage.py createsuperuser --username admin --email admin@root.com
shell:
	python manage.py shell
collstatic:
	python manage.py collectstatic
clean:
	rm -f db.sqlite3 && rm -r appointments/migrations