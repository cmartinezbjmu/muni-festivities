FROM python:3.8-alpine

# Generate requirements.txt file
RUN pip install pipenv
COPY Pipfile* /
RUN pipenv lock --requirements > requirements.txt

# Add dependecy of django postgres driver
#RUN apk update && apk add libpq

# Install uWSGI dependencies
#RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers build-base postgresql-dev
# Install project packages
RUN pip install -r requirements.txt
# Keeps docker lightweight removing temporary installation files
#RUN apk del .tmp

RUN mkdir /app
# Copy project's files
COPY . /app
# Change directory to roles_ms
WORKDIR /app
# Copy scripts dir
COPY ./scripts /scripts
# Updates execution permissions
RUN chmod +x /scripts/*.sh

# Creates directory to holds static files (*.js, *.html, *.css)
RUN mkdir -p /web/static

# Creates a new user (best practices)
RUN adduser -D appUser
RUN chown -R appUser:appUser /web
RUN chmod -R 755 /web
RUN chown -R appUser:appUser /app
RUN chmod -R 755 /app

# Switch to created user
USER appUser