# Composed Server with Docker Compose

This Directory contains the setup for a composed server environment using Docker Compose. The environment consists of a web server (Nginx), a database (PostgreSQL), and a data visualization tool (Adminer).

## Prerequisites

Before getting started, ensure you have the following installed on your machine:
- Docker

Verify the installation by running the following commands in your terminal:

```bash
docker --version
```

## Usage

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/composed-server.git
cd composed-server
```

### Step 2: Start the Composed Environment

Run the following command to start the composed environment:

```bash
docker-compose up -d
```

### Step 3: Testing

- Web Server: Open your browser and navigate to [http://localhost:8081](http://localhost:8081).
- Database and Adminer: Access [http://localhost:8082](http://localhost:8082) in your browser and use Adminer to log in using the provided PostgreSQL credentials.

### Step 4: Stopping the Services

To stop the composed environment, run:

```bash
docker-compose down
```

### Step 5: Cleanup

To remove all stopped containers, networks, and volumes created by Docker Compose, execute:

```bash
docker-compose down --volumes
```

## Customization

Feel free to customize the environment according to your requirements by modifying the `docker-compose.yml` file.


