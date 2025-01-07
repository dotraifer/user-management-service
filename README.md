# User management service

This is a simple user management service that allows you to create,
read, update and delete users.

## Run the project

### Locally

* Clone the project
* configure the database to use in the `config.py` file
* Run 'pip install -r requirements.txt'
* Run `fastapi run main.py`

## On Docker

* Pull the image from docker hub
* Run and Mount the volume(configurations) with the command `docker run -v /path/to/config.yaml:/app/config.yaml -p 8000:8000 user-management-service`
* The service will be available at `http://localhost:8000`