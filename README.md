# Docker Image w/ a Scalable Flask App Directory (+NGINX & uWSGI)

Attempting to provide a base for multi-file Flask micro-services, w/ a working server setup and easy dependency management in Docker.

Goals:
1. Create a base for microservice Flask apps. The db portion is commented out assuming the app is an API-first app.
2. Use Docker as alternative to virtualenv, with added benefit of easy deployment. Assuming that each microservice has it's own Docker instance that can be spun up/down without touching source on other services.
3. Server tutorials tend to stop at the most basic one-page Flask app, but my apps usually get complex enough to need the app factory + blueprints Flask app.

## Instructions (Mac)
1. [Install Docker Engine] (https://docs.docker.com/engine/installation/)
2. Create a default Docker Machine

Using tiangolo's uwsgi-nginx-flask-docker setup, with customization starting at the ini file.

Instructions to come.
