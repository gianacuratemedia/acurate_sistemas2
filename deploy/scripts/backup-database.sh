#!/bin/bash
set -e
#Back up remote database and copies
SERVER=knowtured
echo -e "\n>>> Backuping up database"
TIME=$(date "+%s")
DBNAME="db.$TIME.sqlite3"
ssh root@$SERVER /bin/bash << EOF
set -e
mkdir -p /root/backups/
cp /app/db.sqlite3 /root/backups/$DBNAME
EOF
mkdir -p ~/backups/
scp root@knowtured:/root/backups/* ~/backups/