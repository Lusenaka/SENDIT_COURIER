# SENDIT-API
We are expected to create a set of API endpoints

## API Endpoints covered included in this branch


| Method        |       Endpoint                        |         Description                           |
| ------------- |       -------------                   |         -------------                         |
| `GET`         | `/api/v1/parcel`                      |   Gets all parcel delivery orders             |
| `GET`         | `/api/v1/parcel/<order_id>`           |   Get a parcel delivery orders by id          |
| `POST`        | `/api/v1/parcels`                     |   Create a parcel delivery orders             |
| `GET`         | `/api/v1/users/`                      |   Gets all the users                          |
| `GET`         | `/api/v1/parcels/userorder`              |   Get the orders of a specific user                            |
| `POST`        | `/api/v1/users/signup`                |   Register a user                             |
| `POST`        | `/api/v1/users/login`                 |   Signin a User                               |
| `PUT`         | `/api/v1/parcels/<order_id>/cancel`   |   Cancel the specific parcel delivery order   |


# Preparing your machine

Make sure your system has all the required tools for use e.g Python 3 and pip environments.

# Steps to be followed

Start by making the folder in which the API will be implimented. Simply Open your terminal and type:

```
mkdir SENDIT-API
```

Afterwhich we go into the folder by typing the code:

```
cd SENDIT-API
```

## Create a Virtual Environment for our Project

Create a virtual environment by typing:

```
virtualenv -p python3 .
```

We are required to activate the virtual environment before we install our projects requirements. You can do that by typing:

```
source venv/bin/activate
```

## Clone and Configure a Flask Project

Login into your github account and open the project folder then follow the instruction on how to clone the existing project.

```
git clone https://github.com/AlvinLusenaka/SENDIT-API.git
```

Now you can then install the requirements by typing:

```
pip install -r requirements.txt
```

## Unit Testing
To test the endpointsensure that the following tools are available the follow steps below
   ### Tools:
     Postman
     Unnitest
     
     