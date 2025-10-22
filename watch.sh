#/usr/bin/bash
echo "Updating ..."
cd /home/monica/alzwatch
git pull
echo "Starting ..."
rpicam-vid -t 0 --width 800 --height 600 --framerate 15 --codec libav --libav-format mpegts --libav-audio -o "tcp://0.0.0.0:1234?listen=1" &
/usr/bin/python --version
sleep 2
/usr/bin/python /home/monica/alzwatch/watch.py
sleep 10
pause