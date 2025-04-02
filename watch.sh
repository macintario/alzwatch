#/usr/bin/bash
echo "Updating ..."
cd /home/ivan_/alzwatch
git pull
echo "Starting ..."
python --version
sleep 2
python /home/ivan_/alzwatch/watch.py
sleep 10
pause