# Java Hello World Application with Docker and Maven

This directory contains a simple "Hello World" Java application built with Docker and Maven. The application is configured to run across different Java environments: Java 8, Java 11, and Java 17.

## Project Structure
- `src/main/java/com/example/HelloWorld.java`: Java source code for the "Hello World" application.
- `pom.xml`: Maven configuration file with profiles for different Java versions.
- `Dockerfile`: Multi-stage Dockerfile for building Docker images for each Java version.
- `README.md`: Project documentation.

## Getting Started
To build and run the Java application using Docker and Maven, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/java-docker-maven-helloworld.git
   cd java-docker-maven-helloworld
   ```

2. Build Docker images for each Java version:
   ```bash
   docker build -t helloworld-java8 --target=java8 .
   docker build -t helloworld-java11 --target=java11 .
   docker build -t helloworld-java17 --target=java17 .
   ```

3. Run Docker containers for each Java version:
   ```bash
   docker run --rm helloworld-java8
   docker run --rm helloworld-java11
   docker run --rm helloworld-java17
   ```

4. Verify that the "Hello, World!" message is printed to the console for each Java version.

## Cleanup

After testing, clean up Docker containers and images:

   ```bash
   docker stop $(docker ps -aq)
   docker rm $(docker ps -aq)
   docker rmi helloworld-java8 helloworld-java11 helloworld-java17
   ```

##Additional Notes

- Ensure Docker and Docker Compose are installed on your machine.
- This project demonstrates the usage of Maven profiles to manage different Java versions.
- The Dockerfile utilizes multi-stage builds to optimize Docker images and reduce size.
- Feel free to modify the Java source code or Dockerfile to extend or customize the application.