# simple document repository

[![Build Status](https://travis-ci.org/StoleMyIceCream/simple_document_repository.svg?branch=master)](https://travis-ci.org/StoleMyIceCream/simple_document_repository)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

using django rest framework, postgres. Check out the project's [documentation](http://StoleMyIceCream.github.io/simple_document_repository/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
