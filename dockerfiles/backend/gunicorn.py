"""
Application Configuration File
https://docs.gunicorn.org/en/stable/settings.html#settings
"""
import os
import multiprocessing


# Chdir to specified directory before apps loading.
# https://docs.gunicorn.org/en/stable/settings.html#chdir
chdir = '/app/'

# Bind the application on localhost both on ipv6 and ipv4 interfaces.
# https://docs.gunicorn.org/en/stable/settings.html#bind
bind = '0.0.0.0:5000'


####################
# Worker Processes #
####################

# The number of worker processes for handling requests.
# https://docs.gunicorn.org/en/stable/settings.html#workers
workers = multiprocessing.cpu_count() * 2 + 1

# The number of worker threads for handling requests.
# https://docs.gunicorn.org/en/stable/settings.html#threads
threads = 2 * multiprocessing.cpu_count()

# The maximum number of requests a worker will process before restarting.
# https://docs.gunicorn.org/en/stable/settings.html#max-requests
max_requests = os.getenv('GUNICORN_WORKER_MAX_REQUESTS', default=2400)

# The maximum jitter to add to the max_requests setting.
# https://docs.gunicorn.org/en/stable/settings.html#max-requests-jitter
max_requests_jitter = os.getenv('GUNICORN_WORKER_MAX_REQUESTS_JITTER', default=50)

# Workers silent for more than this many seconds are killed and restarted.
# https://docs.gunicorn.org/en/stable/settings.html#timeout
timeout = os.getenv('GUNICORN_WORKER_TIMEOUT', default=30)
