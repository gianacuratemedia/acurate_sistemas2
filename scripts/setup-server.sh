#!/bin/bash
set -e
#Sets up new server to host Django app
export SERVER=165.227.62.217
DJANGO_SETTINGS_MODULE="knowtured.settings.prod"

#Take secret key as 1st argument
if[[-z "$1"]]
then 
    echo "ERROR: No value set for DJANGO_SECRET_KEY, argument requiered."
    exit 1
else
    DJANGO_SECRET_KEY="$1"
fi

echo -e "\n>>> Setting up $SERVER"
ssh root@$SERVER /bin/bash << EOF
    set -e

    echo -e "\n >>> Updating apt sources"
    apt-get -qq upgrade

    echo -e "\n>>> Installing apt packages"
    apt-get -qq install python3-pip dos2unix tree

    echo -e "\n>>>Installing virualenv"
    pip3 install virtualenv

    echo -e "\n>>> Setting up project folder"
    mkdir -p /app/logs

    echo -e "\n>>> Creating our virtualenv"
    if [[ ! -d "/app/env"]]
    then
        virtualenv -p python3 /app/env
    else
        echo ">>>Skipping virtualenv creatiom - already present"
    fi

    echo -e "\n>>> Setting system enviroment variables"

    if [[  "\$DJANGO_SETTINGS_MODULE" != "$DJANGO_SETTINGS_MODULE"]]
    then
        echo "DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE" >> /etc/enviroment
    else
        echo ">>> Skipping DJANGO_SETTINGS_MODULE - already present"
    fi

    if [[ "\$DJANGO_SECRET_KEY" != "$DJANGO_SECRET_KEY"]]
    then 
        echo "DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY" >> /etc/environment
    else
        echo ">>> Skipping DJANGO_SECRET_KEY - already present"
    fi

EOF

./scripts/upload-code.sh 

ssh root@$SERVER /bin/basj << EOF
    set -e

    echo -e "\n Deleting old files"
    rm -rf /app/knowtured
    rm -rf /app/config
    rm -rf /app/scripts
    rm -f /app/requirements.txt

    echo -e "\n>>> Copying new files"
    cp -r /root/deploy/knowtured /app/
    cp -r /root/deploy/config /app/
    cp -r /root/deploy/scripts /app/
    cp /root/deploy/requirements.txt /app/

    echo -e "\n>>> Installing Python packages"
    cd /app/
    . env/bin/activate
    pip install -r /app/requirements.txt

    echo -e "\n>>> Running Django migrations"
    pushd knowtured
    ./manage.py migrate

    echo -e "\n>>> Collecting static files"
    ./manage.py collectstatic
    popd

    echo -e "\n>>> Starting Supervisord"
    supervisord -c config/supervisord.conf
EOF

echo -e "\n>>> Done Setting up $SERVER"