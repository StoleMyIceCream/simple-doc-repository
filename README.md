
# Doc Repository

[![CI/CD Status](https://github.com/StoleMyIceCream/simple-doc-repository/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/StoleMyIceCream/simple-doc-repository/actions)

## Overview

Your Project Name is a REST API designed to receive and save files. It provides a simple yet flexible solution for handling file uploads, allowing storage both locally and in cloud services like AWS.

## Features

- **File Upload:** Receive and save files through API endpoints.
- **Local Storage:** Save files locally on the server.
- **AWS Integration:** Optionally configure the API to store files in Amazon S3.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django Rest Framework
- Docker

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Install dependencies:

# Local Development
  
  Start the dev server for local development:
  ```bash
  docker-compose up --build
  ```
  
  Run a command inside the docker container:
  
  ```bash
  docker-compose run --rm web [command]
  ```

3. Configure your environment:

   - Copy the `.env.example` file to `.env` and adjust the settings.

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The API will be accessible at [http://localhost:8000/](http://localhost:8000/).

## Usage

1. **File Upload Endpoint:**
   - Use the `/files/` endpoint to submit files. Configure the storage location in your settings.

2. **API Documentation:**
   - Explore the API using the interactive documentation available at [http://localhost:8000/swagger/](http://localhost:8000/swagger/) or [http://localhost:8000/redoc/](http://localhost:8000/redoc/).

## Configuration

- **Local Storage:**
  - Set `LOCAL_STORAGE = True` in your settings to store files locally.

- **AWS S3 Storage:**
  - Set `AWS_STORAGE = True` and configure your AWS credentials and S3 bucket settings in the settings file.

## CI/CD Pipeline

The project includes a CI/CD pipeline using GitHub Actions. On each push to the `main` branch, the pipeline runs tests and, if successful, deploys the application.

## Contributing

We welcome contributions! Please follow our [Contribution Guidelines](CONTRIBUTING.md) for details.

## License

This project is licensed under the [MIT License](LICENSE).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  


