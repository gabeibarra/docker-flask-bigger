# Docker + A Scalable Flask App Directory (+NGINX & uWSGI)

Attempting to provide a base for multi-file Flask projects, working server setup, and easy dependency management in Docker.

Goals:
1. Create a base for microservice Flask apps. The db portion is commented out assuming the app is an API-first app.
2. Use Docker as alternative to virtualenv, with added benefit of easy deployment. Assuming that each microservice has it's own Docker instance that can be spun up/down without touching source on other services.
3. Server tutorials tend to stop at the most basic one-page Flask app, but my projects and team always uses the app factory + blueprints Flask app.
 

This is using tiangolo's uwsgi-nginx-flask-docker setup, with customization starting at the ini file.

Instructions to come.
