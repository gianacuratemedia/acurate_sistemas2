#!/bin/bash
set -e
SERVER="knowtured"
echo -e "\n>>> Copying Django project files to server."

echo -e "\n>>> Preparing Scripts locally."
rm -rf deploy
mkdir deploy 
cp -r config deploy
cp -r scripts deploy
cp -r knowtured deploy
cp requirements.txt deploy

echo -e "\n>>> Copying files to server."
ssh root@$SERVER "rm -rf /root/deploy"
scp -r deploy root@$SERVER:/root/

echo -e "\n>>> ------------ ls deploy ---------------------"
ssh root@$SERVER "ls deploy"

echo -e "\n>>>Cleaning up deployed files on the server."
ssh root@$SERVER /bin/bash << EOF
    set -e
    find /root/deploy/ -name *.pyc -delete
    find /root/deploy/ -name __pycache__ -delete
    find /root/deploy -type f -print0 | xargs -0 dos2unix
EOF

echo -e "\n>>> Finish copying Django project files to server."

