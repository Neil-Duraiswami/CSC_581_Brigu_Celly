# Stage for Java 8
FROM openjdk:8-jdk-alpine as java8build
WORKDIR /app
COPY . .
RUN apk add --no-cache maven
RUN mvn clean package -PJava8
CMD ["java", "-jar", "/app/target/hello-world-java-1.0-SNAPSHOT.jar"]

# Stage for Java 11
FROM openjdk:11-jdk as java11build
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y maven
RUN mvn clean package -PJava11
CMD ["java", "-jar", "/app/target/hello-world-java-1.0-SNAPSHOT.jar"]

# Stage for Java 17
FROM amazoncorretto:17 as java17build
WORKDIR /app
COPY . .
RUN yum update -y && yum install -y maven
RUN mvn clean package -PJava17
CMD ["java", "-jar", "/app/target/hello-world-java-1.0-SNAPSHOT.jar"]




