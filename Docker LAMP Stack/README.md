# Docker Compose LAMP Stack

This repository contains files and instructions to set up a LAMP (Linux, Apache, MySQL, PHP) stack using Docker Compose.

## Objective

The objective of this project is to deepen understanding of Docker Compose by creating a comprehensive LAMP stack. This exercise covers configuring inter-container networking, volume management for data persistence, and basic PHP scripting to interact with a MySQL database.

## Prerequisites

- Docker and Docker Compose installed on your computer.
- Basic knowledge of YAML, PHP, SQL, and command-line operations.

## Steps to Setup

1. **Environment Setup and Docker Compose File**
   - Created a directory named `lamp-project`.
   - Created subdirectories `www` for PHP files and `mysql` for database persistence.
   - Created a Docker Compose file named `docker-compose.yml`.
   - Defined services for web, db, and admin.
   - Configured networking and volumes.

2. **Creating a PHP Script**
   - Created a PHP script `index.php` inside the `www` folder.
   - Developed a script to connect to MySQL database and display a message.

3. **Running and Testing**
   - Started the LAMP stack using `docker-compose up -d`.
   - Accessed PHP application at [http://localhost:8080](http://localhost:8080).
   - Accessed phpMyAdmin at [http://localhost:8081](http://localhost:8081).

4. **Cleanup and Documentation**
   - Stopped services and cleaned up using `docker-compose down --volumes`.
   - Provided documentation including challenges faced and solutions.

## Challenges Faced
- Initially encountered a missing MySQLi extension error when connecting PHP to MySQL database.
- Resolved by creating a custom Dockerfile to install MySQLi extension.

## Deliverables
- Screenshots of PHP application and phpMyAdmin interface.
- Contents of `docker-compose.yml`, `Dockerfile`, `000-default.conf`, and `index.php` files.

