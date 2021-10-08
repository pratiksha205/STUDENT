# STUDENT project

## How to setup project?

### Clone the project from Gitlab using HTTPS

```sh
git clone https://github.com/pratiksha205/STUDENT.git
```

## create virtual environment
```sh
virtualenv venv
```

```sh
## activate virtual environment
$ source venv/bin/activate
```

## install the dependencies

(venv)$ pip install -r requirements.txt

## Run the migrations
(venv)$ cd STUDENT
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate

## Run the server
(venv)$ cd STUDENT
(venv)$ python manage.py runserver