#/usr/bin/bash
echo "Updating ..."
cd /home/ivan_/alzwatch
git pull
echo "Starting ..."
/usr/bin/python --version
sleep 2
/usr/bin/python /home/ivan_/alzwatch/watch.py
sleep 10
pause