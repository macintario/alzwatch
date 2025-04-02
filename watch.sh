#/usr/bin/bash
echo "Updating ..."
cd /home/ivan/alzwatch
git pull
echo "Starting ..."
python /home/ivan_/alzwatch/watch.py