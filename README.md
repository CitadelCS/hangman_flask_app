# Hangman Flask App

The Hangman Flask App is a fun, interactive web-based game where players guess a word one letter at a time to avoid 'hanging'. This Flask application is containerized for ease of deployment using Docker.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Tutorials](#tutorials)
  - [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
  - [Docker](#docker)
  - [Docker Swarm](#docker-swarm)
- [Development](#development)
- [Authors](#authors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

### Tutorials

For more information on using Docker and deploying applications, consider the following tutorials:

    [Docker 101 Tutorial](https://www.docker.com/101-tutorial/)
    [Swarm Mode Tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/)
    Heroku cost!
    [Heroku GitHub Integration](https://devcenter.heroku.com/articles/github-integration)
    [DevSecOps Tutorial for Beginners | CI Pipeline with GitHub Actions and Docker Scout](https://www.youtube.com/watch?v=gLJdrXPn0ns)

##### Installation

A step by step series of examples that tell you how to get a development env running.

Clone the repo:

bash

git clone https://github.com/rowingsjr/hangman_flask.git

Navigate to the cloned directory:

bash

cd hangman_flask

Build the Docker image:

bash

docker build -t hangman_flask .

Run the Docker container:

bash

docker run -p 5000:5000 hangman_flask

The app should now be running on localhost:5000.

## Usage

Here you can include a fun example of how to play the game or how to interact with the app.

## Deployment

Additional notes about how to deploy this on a live system.

### Docker

Run the container in detached mode with the following command:

bash

docker run -d -p 5000:5000 hangman_flask

### Docker Swarm

Initialize Docker Swarm:

bash

docker swarm init

Deploy the stack:

bash

docker stack deploy -c docker-compose.yml hangman_stack

The application will be accessible at http://localhost:5000 or the IP of any Docker Swarm node.

## Development

If you wish to develop the app, you can mount a volume to the Docker container to allow for live editing of the Flask application files.

## Authors

    Richard Owings Jr - Graduate Student MS Computer Science - Initial work and development of project - rowingsjr

See also the list of contributors who participated in this project.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

    Special Ackonwledgment to Dr. Verdicchio for allowing this to be a success. 

```bash
docker
docker-compose
