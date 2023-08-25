#!/bin/sh
#
# Prepares the environment and starts the application
#

apk add python3 py3-pip

python3 -m pip install pika pyp8s

python3 /app/app_rabbitmq_loopback.py
