# patientsManager
Manage your patients consultation

## Installation Dev:
Requirements
- Docker
- Docker compose
- python >= 3.10

- Clone this repo

On shell
```
cd patientsManager
```
```
docker-compose build
```

## First run:
On shell

```
docker-compose up -d
```

Populate database with 5000 patient (you can modify number if you want)

```
docker-compose app python app/manage.py runscript create_some_patients --script-args 5000
```

Create first user:

```
docker-compose run python app/manage.py runscript create_first_user_for_dev
```

## Run app

Open browser, and go to '0.0.0.0:8000/patients'

Login: Shinji

Pass: ReiEva00

(you can modify login and pass with in script 'create_first_user_for_dev.py')

## Local dev

Create and activate python venv

```
python -m venv venv
```

```
source venv/bin/activate
```

```
pip install --upgrade pip && pip install -r manager/requirements.txt
```


### optional

Create a superUser to access admin

```
docker-compose run app python app/manage.py createsuperuser --username=YouName --email=YourMail@example.com
```

Shell will ask you the password
