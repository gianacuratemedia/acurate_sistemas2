#!/bin/bash
set -e
#Deploy Django project.
#export SERVER=servername
export SERVER=knowtured
./scripts/backup-database.sh
./scripts/code-upload.sh
./scripts/install-code.sh