#!/bin/bash
/usr/src/app/wait-for-it.sh db:5432 --timeout=30 -- echo "Database is up"
exec "$@"