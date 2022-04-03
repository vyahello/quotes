![Screenshot](media/logo.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/vyahello/quotes.svg?branch=master)](https://travis-ci.org/vyahello/quotes)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/pylint-checked-blue)](https://www.pylint.org)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with pydocstyle](https://img.shields.io/badge/pydocstyle-checked-yellowgreen)](http://www.pydocstyle.org/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![CodeFactor](https://www.codefactor.io/repository/github/vyahello/quotes/badge)](https://www.codefactor.io/repository/github/vyahello/quotes)
[![Docker pulls](https://img.shields.io/docker/pulls/vyahello/quotes.svg)](https://hub.docker.com/repository/docker/vyahello/quotes)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fpep8-checker.herokuapp.com)](https://quote-quote.herokuapp.com)

# Quotes

> Simple web application to show quotes of famous people.
>
> It is built with **django** python web framework.

_**Note**: please take into account that it is built for demo purpose but not for actual usage._

## Tools

### Production

- front-end
  - html5
  - css3
- back-end
  - python 3.6, 3.7, 3.8
  - [django](https://www.djangoproject.com/) web framework
- [docker](https://www.docker.com/) >= 18.0

### Development 

- [pytest](https://pypi.org/project/pytest/)
- [black](https://black.readthedocs.io/en/stable/)
- [mypy](http://mypy.readthedocs.io/en/latest)
- [pylint](https://www.pylint.org/)
- [flake8](http://flake8.pycqa.org/en/latest/)
- [pydocstyle](https://github.com/PyCQA/pydocstyle)
- [travis](https://travis-ci.org/)

## Usage

![Usage](media/usage.gif)

### Quick start 

Please discover app via:
  - https://quote-quote.herokuapp.com (prod stage)
  - http://178.62.222.165:5003 (test stage)

### Docker

```bash
docker run --rm -it -p 3000:5001 vyahello/quotes:<version> quotes
```

> Please access an application via http://0.0.0.0:3000 endpoint

### K8S 

```bash
kubectl create deployment hello-world-rest-api --image=vyahello/quotes 
kubectl expose deployment hello-world-rest-api --type=LoadBalancer --port=3000
```

> Please access an application via http://0.0.0.0:3000 endpoint

### Source code

```bash
python quotes/manage.py runserver
```

> Please access an application via http://127.0.0.1:8000 endpoint

**[⬆ back to top](#quotes)**

## Development notes

### REST API

Rest api is build with `djangorestframework` and `drf-yasg` (swagger) libraries.

Here are available api endpoints:
- `/api`: 
  - `GET`: _Retrieves all quotes_
  - `POST`: _Creates a new quote_
- `/api/<id>`:
  - `GET`: _Retrieves a single quote by it's id_
  - `PUT`: _Updates a single quote by it's id_
  - `DELETE`: _Deletes a quote by it's id_

> Please refer to `/api/docs` endpoint which provides a neat swagger REST API documentation.

### Setup
> Please use it as a reference to create/manage fresh django application
```bash
django-admin startproject manager  # create application manager
django-admin startapp app  # create application source
python quotes/manage.py makemigrations  # add new model (if exists) to database
python quotes/manage.py migrate  # sync models with database
python quotes/manage.py shell  # start interactive shell
python quotes/manage.py createsuperuser  # create user for administration
```

To manage an application please use `/admin` endpoint.

Please use `admin` superuser for management.

### Docker 

Please use the following [example notes](https://github.com/vyahello/pep8-checker#development-notes) to proceed with docker image provisioning.

### K8S

It is possible to orchestrate app via kubernetes, the following command will launch 3 instances of app.

```bash
kubectl apply -f deployment.yaml
kubectl get pods
NAME                      READY   STATUS    RESTARTS   AGE
quotes-6f64474dc5-7ct8t   1/1     Running   0          4m49s
quotes-6f64474dc5-95cx8   1/1     Running   0          4m49s
quotes-6f64474dc5-dg5n8   1/1     Running   0          4m49s
```

### Testing

Generally, `pytest` tool is used to organize testing procedure.

Please follow next command to run only **unit** tests:
```bash
pytest -m unit
```

Or only **api** tests:
```bash
pytest -m api
```

Or only **web** tests, eventually:
```bash
pytest -m web
```

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `pylint`, `flake8`, `mypy`, `pydocstyle`) and unittests (`pytest`) will be run automatically after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
./analyse-source-code.sh
```
### Release notes

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta

Author – _Volodymyr Yahello_. Please check [authors](AUTHORS.md) file for more details.

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (git checkout -b feature/fooBar)
6. Commit your changes (git commit -am 'Add some fooBar')
7. Push to the branch (git push origin feature/fooBar)
8. Create a new Pull Request

### What's next

All recent activities and ideas are described at project [issues](https://github.com/vyahello/quotes/issues) page. 
If you have ideas you want to change/implement please do not hesitate and create an issue.

**[⬆ back to top](#quotes)**
