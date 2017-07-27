# this shell script is put in image: jasko/log-collect
# this script use for synchronize logfiles from original path to another place, and print out a time message to show the synchonize is keeping
# options use environments
# $HOSTNAME: podname ; $LOGOPT: rsync options ; $LOG_LOCATION: original log path ; $INTERVAL: sync per every time

##!/bin/bash
#mkdir -p /mnt/pods/$HOSTNAME
#while true; do
#  rsync $LOGOPT $LOG_LOCATION /mnt/pods/$HOSTNAME
#  T=$(date)
#  echo $T " [log collected]"
#  sleep $INTERVAL
#done

#!/bin/bash

python gethn.py

myFile="/cid.txt"
while :
do
  echo 'checking'
  sleep 3
  if [ -f "$myFile" ] && grep -q "docker://" /cid.txt
  then  
    break
  else
    python gethn.py
  fi    
done
echo "ok"

STR=$(cat /cid.txt)
PROJCON=${STR:9:12}
#mkdir -p /mnt/pods/$HOSTNAME
mkdir -p /mnt/pods/$PROJCON
while true; do
  rsync $LOGOPT $LOG_LOCATION /mnt/pods/$PROJCON
  T=$(date)
  echo $T " [log collected]"
  sleep $INTERVAL
done

