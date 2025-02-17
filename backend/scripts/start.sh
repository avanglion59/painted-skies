#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python3 manage.py migrate
python3 manage.py collectstatic --noinput --verbosity 0
python3 manage.py runserver_plus 0.0.0.0:8000
