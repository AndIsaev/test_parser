#!/bin/bash
set -eu
flask --app backend.app db upgrade --directory=backend/migrations
flask --app backend.app run --host=0.0.0.0 --reload