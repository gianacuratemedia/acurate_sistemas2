#!/bin/bash
#Install Django app on server.
set -e
SERVER="knowtured"
echo -e "\n>>> Install Django project files on server."

ssh root@$SERVER /bin/bash << EOF
SERVER="knowtured"
set -e  
echo -e "\n >>> Stopping Gunicorn"
cd /app/
. env/bin/activate
./scripts/super.sh stop gunicorn

echo -e "\n  >>> Deleting old files"
rm -rf /app/$SERVER
rm -rf /app/config
rm -rf /app/scripts
rm requirements.txt

echo -e "\n  >>> Copying new files"
cp -r /root/deploy/$SERVER /app/
cp -r /root/deploy/config /app/
cp -r /root/deploy/scripts /app/
cp /root/deploy/requirements.txt /app/

echo -e "\n  >>> installing python packages"
pip install -r requirements.txt
pip freeze

echo -e "\n  >>> Run Django Migrations"
pushd $SERVER
./manage.py migrate

echo -e "\n  >>> Collecting Static Files"
./manage.py collectstatic
popd

echo -e "\n >>> Re-loading our Supervisord config"
./scripts/super.sh reread

echo -e "\n >>> Starting Gunicorn"
./scripts/super.sh start gunicorn

EOF

echo -e "\n >>> Finished Installing Django project on server."

