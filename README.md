# APi End-Points with basic CRUD Operations

##  Description

Building and api endpoint that performs CRUD Operations on s person object, as partial fulfilment of the requiremnts of the HNG Internship Programme

###  Directory Structure

```
├── database.py
├── hng2.db
├── __init__.py
├── main.py
├── models.py
├── __pycache__
│   ├── database.cpython-310.pyc
│   ├── main.cpython-310.pyc
│   ├── models.cpython-310.pyc
│   └── schemas.cpython-310.pyc
├── README.md
├── requirements.txt
├── schemas.py
└── Spacefile

```

###  Features

-  C - creating New Person Object

-  R - reading exsiting person

-  U - updating existing person details

-  D - deleting existing person


##  Getting Started

Getting started developing with this api is as follows

```shell script
# Clone the repository
git clone https://github.com/baccrie/HNG_Stage2

# cd into project root
cd HNG Stage2

# install project depenedncies
pip3 install -r requirements.txt

# create virtual enviroment
python3 -m venv env

# activate virtual enviroment
source env/bin/activate

# start the api
uvicorn main:app --reload
```

Afterwards, the project will be live at [http://localhost:8000](http://localhost:8000).

## Documentation

FastAPI automatically generates documentation based on the specification of the endpoints for this projects. You can find the docs at [http://localhost:5000/docs](http://localhost:5000/docs).

## Testing



# Code Formatting & Linting
