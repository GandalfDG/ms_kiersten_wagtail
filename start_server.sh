#!/usr/bin/bash

APP_PATH="/home/jackc/ms_kiersten_wagtail/ms_kiersten/"
BIND_ADDR="127.0.0.1:8888"
PIDFILE="../gunicorn_pid"

cd $APP_PATH
source env/bin/activate

python -m gunicorn --bind $BIND_ADDR --daemon --pid $PIDFILE \
	--env DJANGO_SETTINGS_MODULE=ms_kiersten.settings.production \
	--user root
