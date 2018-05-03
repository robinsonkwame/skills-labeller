#!/bin/bash
cd /skills-labeller/dispatcher
gunicorn --reload --bind=0.0.0.0:8000 __init__:__hug_wsgi__
