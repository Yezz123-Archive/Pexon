![Pexon-Rest-API](.github/header.svg)

# Pexon-Rest-API

A full Rest-API for request & response a JSON file, Building a Simple WorkFlow that help you to Request a JSON File Format and Handling the Same Format for Response. Also with a container side for Docker 🛠

## Getting Started

- As Python grows in popularity, the variety of high-quality frameworks available to developers has blossomed. In addition to steadfast options like Django and Flask, there are many new options including FastAPI.

### Prerequisites

- Python 3.6 or higher
- FastAPI
- Docker

### Project setup

```sh
# clone the repo
$ git clone https://github.com/yezz123/Pexon-Rest-API

# move to the project folder
$ cd Pexon-Rest-API
```

### Creating virtual environment

- Install `pipenv` a global python project `pip install pipenv`
- Create a `virtual environment` for this project

```shell
# creating pipenv environment for python 3
$ pipenv --three

# activating the pipenv environment
$ pipenv shell

# if you have multiple python 3 versions installed then
$ pipenv install -d --python 3.8

# install all dependencies (include -d for installing dev dependencies)
$ pipenv install -d
```

### Running the Application

- To run the [Main](main.py) we need to use [uvicorn](https://www.uvicorn.org/) a lightning-fast ASGI server implementation, using uvloop and httptools.

```sh
# Running the application using uvicorn
$ uvicorn main:app

## To run the Application under a reload enviromment use -- reload
$ uvicorn main:app --reload
```

- Here we can Switch Between using [SWAGGER UI](https://swagger.io/tools/swagger-ui/) or [Redoc](https://redocly.github.io/redoc/) to Play around the API.

## Running the Docker Container

- We have the Dockerfile created in above section. Now, we will use the Dockerfile to create the image of the FastAPI app and then start the FastAPI app container.

```sh
$ docker build
```

- list all the docker images and you can also see the image `pexon:latest` in the list.

```sh
$ docker images
```

- run the application at port 5000. The various options used are:

> - `-p`: publish the container's port to the host port.
> - `-d`: run the container in the background.
> - `-i`: run the container in interactive mode.
> - `-t`: to allocate pseudo-TTY.
> - `--name`: name of the container

```sh
$ docker container run -p 5000:5000 -dit --name Pexon-Rest-API pexon:latest
```

- Check the status of the docker container

```sh
$ docker container ps
```

## Preconfigured Packages

Includes preconfigured packages to kick start Pexon by just setting appropriate configuration.

| Package                                                      | Usage                                                            |
| ------------------------------------------------------------ | ---------------------------------------------------------------- |
| [uvicorn](https://www.uvicorn.org/)        | a lightning-fast ASGI server implementation, using uvloop and httptools.           |
| [Python-Jose](https://github.com/mpdavis/python-jose) | a JavaScript Object Signing and Encryption implementation in Python.    |
| [SQLAlchemy](https://www.sqlalchemy.org/)  | is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. |
| [starlette](https://www.starlette.io/)   | a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.    |
| [passlib](https://passlib.readthedocs.io/en/stable/)  | a password hashing library for Python 2 & 3, which provides cross-platform implementations of over 30 password hashing algorithms         |
| [bcrypt](https://github.com/pyca/bcrypt/)               | Good password hashing for your software and your servers.    |
| [python-multipart](https://github.com/andrew-d/python-multipart) | streaming multipart parser for Python.   |

`yapf` packages for `linting and formatting`

## Contributing

- Join the Pexon-Rest-API Creator and Contribute to the Project if you have any enhancement or add-ons to create a good and Secure Project, Help any User to Use it in a good and simple way.

## License

This project is licensed under the terms of the [MIT license](LICENSE).