
virtualenv -p ~/.pyenv/versions/3.7.10/bin/python venv

source venv/bin/activate

pip install -r requirements.txt

django-admin startproject secret_santa
cd secret_santa
python manage.py startapp ssweb