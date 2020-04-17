![Screenshot](icon.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/vyahello/quotes.svg?branch=master)](https://travis-ci.org/vyahello/quotes)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/quotes/badge.svg?branch=master)](https://coveralls.io/github/vyahello/quotes?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/pylint-checked-blue)](https://www.pylint.org)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with pydocstyle](https://img.shields.io/badge/pydocstyle-checked-yellowgreen)](http://www.pydocstyle.org/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![CodeFactor](https://www.codefactor.io/repository/github/vyahello/quotes/badge)](https://www.codefactor.io/repository/github/vyahello/quotes)

# Quotes

> Simple web application to show quotes of famous people https://quote-quote.herokuapp.com.
>
> It is built with **django** python web framework.

_**Note**: please take into account that it is built for demo purpose but not for actual usage._

## Tools

- python 3.6 | 3.7 | 3.8
- [django](https://www.djangoproject.com/) web framework
- [travis](https://travis-ci.org/) CI
- code analysis
  - [pytest](https://pypi.org/project/pytest/)
  - [black](https://black.readthedocs.io/en/stable/)
  - [mypy](http://mypy.readthedocs.io/en/latest)
  - [pylint](https://www.pylint.org/)
  - [flake8](http://flake8.pycqa.org/en/latest/)
  - [pydocstyle](https://github.com/PyCQA/pydocstyle)

## Usage

![Usage](usage.gif)

### Quick start 

Please use https://quote-quote.herokuapp.com deployed application.

### Docker

```bash
docker run --rm -it -p 3000:5001 vyahello/quotes:<version> quotes
```

Then please access an application via http://0.0.0.0:3000 endpoint

### Source code

```bash
python quotes/manage.py runserver
```

Then please access an application via http://127.0.0.1:8000 endpoint

## Development notes

### Pre setup
> Please use it as a reference to create/manage fresh django application
```bash
django-admin startproject manager  # create application manager
django-admin startapp app  # create application source
python quotes/manage.py makemigrations  # add new model (if exists) to database
python quotes/manage.py migrate  # sync models with database
python quotes/manage.py shell  # start interactive shell
python quotes/manage.py createsuperuser  # create user for administration
```

### Admin management

To manage an application please use http://127.0.0.1:8000/admin endpoint.

Please use `admin` superuser for management.

### REST Api

Rest api is build with `djangorestframework` followed by https://www.django-rest-framework.org documentation.

Here are available api endpoints:

- `/api`: _Retrieves all quotes_
- `/api/<id>`: _Retrieves a single quote by it's id_

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
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
