# Django Rest Framework

This is Django Rest Framework based app. In this we create company and team using rest api.

Clone the project using

```bash
git clone https://github.com/patelsmit57/company-team-rest-api.git
```

<b> SET UP INSTRUCTIONS </b>

First Install docker then

check docker properly Install or not and also check version
```bash
docker --version
```

this command run on terminal for docker set up
```bash
docker build .
```
```bash
docker-compose build
```
```bash
docker-compose up
```
All API end points can be see at   http://127.0.0.1:8000/api/  open website


you carete user
```bash
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```


you can use Postman or vscode Thunder Client for api.

then first generate token

method == POST    http://127.0.0.1:8000/api/token/
```bash
{
  "username":"xxx",
  "password":"xxxxxxx"
}
```

You can test api

first you can create company

method == POST     http://127.0.0.1:8000/api/company/

```bash
{
    "name": "xx",
    "CEO": "xx",
    "address": "xx",
    "Inception_date": "xxxx-xx-xx"
}
```

you can see the detail about company using

method == GET   http://127.0.0.1:8000/api/company/46755041-e6ec-4ea9-a9f3-964cbb98b6f4/

46755041-e6ec-4ea9-a9f3-964cbb98b6f4 is comapny uuid insert your comapny uuid


In this company created team

method == POST  http://127.0.0.1:8000/api/company/46755041-e6ec-4ea9-a9f3-964cbb98b6f4/team/

46755041-e6ec-4ea9-a9f3-964cbb98b6f4 is comapny uuid insert your comapny uuid

```bash
{
    "Lead_Name": "team lead name"
}
```

all team detail see using

method == GET http://127.0.0.1:8000/api/team/


search comapny name and receive the detail

method == POST   http://127.0.0.1:8000/api/search/

```bash
{
    "name": "comapny name"
}
```
