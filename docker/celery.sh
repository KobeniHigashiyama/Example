#!/bin/bash

if [[ "${1}" == "celery" ]]; then
    celery --app=app.tasks.cele:celery worker -l INFO
elif [[ "${1}" == "flower" ]]; then
    celery --app=app.tasks.cele:celery flower
fi