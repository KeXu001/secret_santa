
virtualenv -p ~/.pyenv/versions/3.7.10/bin/python venv

source venv/bin/activate

pip install -r requirements.txt

django-admin startproject secret_santa
cd secret_santa
python manage.py startapp ssweb

python manage.py migrate --run-syncdb
python manage.py collectstatic

python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'