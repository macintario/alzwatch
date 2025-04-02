#/usr/bin/bash
echo "Updating ..."
cd /home/ivan_/alzwatch
git pull
echo "Starting ..."
python --version
python /home/ivan_/alzwatch/watch.py