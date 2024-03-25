FROM php:7.4-apache

# Install MySQLi extension
RUN docker-php-ext-install mysqli

# Copy Apache vhost file to proxy php requests to php-fpm container
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
