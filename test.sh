#!/bin/bash

PORTS=({$start_port..$end_port})
for i in "${PORTS[@]}"
do
  echo $i
done


echo "===== Concourse Params Test ====="
echo "Device IP : $DEVICE_IP"
echo "Username  : $USERNAME"
echo "Message   : $MESSAGE"
echo "================================="
