# Simple Web Server with Docker Compose

This project demonstrates setting up a simple web server using Docker and Docker Compose. The web server serves a basic HTML page using Nginx.

## Prerequisites

Before getting started, ensure you have the following installed on your machine:

- Docker
- Docker Compose
- Basic understanding of Docker concepts and YAML file format
- Basic knowledge of web server operations and HTML

## Getting Started

### Clone the Repository

```sh
git clone https://github.com/Neil-Duraiswami/CSC_581_Brigu_Celly.git

## Navigate to Project Directory

```sh
cd CSC_581_Brigu_Celly/simple-web-server

## Set Up Your Project

-Create an index.html file with your HTML content in the html directory.
-Define your Docker Compose services in the docker-compose.yml file.

## Start the Web Server

```sh
docker-compose up -d

## Access the Web Server

Open your web browser and go to http://localhost:8081 to view the served HTML page.

## Stop the Web Server

```sh
docker-compose down

## File Structure

- `html/`: Directory containing the HTML files served by the web server.
- `docker-compose.yml`: Configuration file defining the Docker services.
