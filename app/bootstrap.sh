#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn app.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers $NUM_WORKERS
    