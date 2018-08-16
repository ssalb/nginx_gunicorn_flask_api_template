# Scalable and containerised Flask REST API template for Keras Deep Learning Models

## Overview
This is a template using Docker containers to deploy a pre-trained Keras model REST API using nginx, gunicorn, redis and flask. It is partially based on the following article:

https://www.pyimagesearch.com/2018/02/05/deep-learning-production-keras-redis-flask-apache/

but pay attention, it's not equivalent.

It is composed of three Docker images:
  - `api`: running the API using Flask and gunicorn
  - `redis`: simply working as a queue to manage requests
  - `nginx`: used as a load balancer

In this way, clients connect to the `nginx` instance, which acts as a proxy and forwards the requests to the servers. The servers here are the `api` instances that you want running (two in this repo as an example), where each of them is linked to it's own `redis` instance.

If you have some experience using flask (or other web frameworks), you'll find that you can easily use the same template for your app.

PS: Honestly, I don't know whether having one `redis` instance per `api` instance is a good decision; perhaps multiple `api` instances could be linked to the same `redis` database. Advice on this, or any other improvement, are most certainly welcome.

## TODO
  - Finish this readme
  - At the moment the API is extremely incomplete - since I've worked with flask before, I focused first on the base infrastructure.

## How to deploy
Assuming you have docker-compose installed (look here if you don't: https://docs.docker.com/compose/install/) simply run:
```
$ docker-compose build
$ docker-compose up
```

## How to actually use it
This is meant to be a template for flask APIs, using Keras deep learning models in particular, but it doesn't do much right now as each application would have it's own special functionalities. You'll need to implement a few functions at least, and probably edit the `api/requirements.txt` file if you want to modify/extend it to your needs. Additionally, you might want to edit the ports in `docker-compose.yml`, as well as `nginx/nginx_flask.conf`.
