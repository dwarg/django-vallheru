# django-vallheru
Python &amp; Django implementation of Vallheru engine.

# install dependency
pip install -r requirements.txt
# migrations
python manage.py migrate
# load fixtures
python manage.py loaddata vallheru/fixtures/sites.json
# create super user
python manage.py createsuperuser
# start server
python manage.py runserver
