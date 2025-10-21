#/usr/bin/bash
echo "Updating ..."
cd /home/monica/alzwatch
git pull
echo "Starting ..."
/usr/bin/python --version
sleep 2
/usr/bin/python /home/monica/alzwatch/watch.py
sleep 10
pause