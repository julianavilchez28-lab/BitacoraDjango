#!/usr/bin/env bash
# Salir inmediatamente si un comando falla
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
