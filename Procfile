release: python manage.py makemigrations && python manage.py migrate
web: gunicorn conf.wsgi --log-file -
celery: celery -A conf worker -B -l info