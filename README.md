# Minstuma
This is a mini student management platform dubbed minstuma

## Application specs
1. User can create students data to manage and write notes on them
1. User can update students
1. User can delete students
1. User can view student details

## Current Api's
All student data apis can be found under   ->   /api/students

## Getting Started

Fork this repository or clone it to your local machine on ubuntu use the following commands
```
git clone 
```

### Prerequisites

1. You will need to install the following for you you to be able to run the following application in your local machine.
* Python version 3.8.10
* postgres database

### Installing

A step by step series of examples that tell you how to get a development env running

1. set up a virtual environment using the following command

```
python3.6 -m venv virtual
```

And activate it

```
source virtual/bin/activate
```

1. Install the requirements in the requirements.txt file using
```
pip install -r requirements.txt
```
1. create a .env file in your rootfolder and add the following configurations
```
SECRET_KEY='<random-string>'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='postgres://databaseowner:password@localhost/databasename'
```
1. create postgres database
```
CREATE DATABASE <your-database-name>
```
1. create a migration using the following command
```
python3.6 manage.py makemigrations
```

and migrate
```
python3.6 manage.py migrate
```
1. create a admin account
```
python 3.6 manage.py createsuperuser
```
and add your credentials

1. run the application using 
```
python3.6 manage.py runserver
```
1. navigate to the admin panel by typing 
```
localhost:8000/admin
```

## Running the tests

Run the system test by typing the following commands
```
python3.6 manage.py tests
```

## Deployment

View the following [document](https://github.com/jakhax/deploying-django-to-heroku-manual) inorder to deploy to a live system

## Built With

* [Django](https://www.djangoproject.com/download/) - The web framework used
* [Bootstrap](https://getbootstrap.com) - The css toolkit used
* Html
* Python


## Author

* **Kingecha Kevin Nyota** - *Initial work* - [Nyota254](https://github.com/Nyota254)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details