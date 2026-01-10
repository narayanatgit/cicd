#!/bin/sh

check_ports() {
  echo "Port: $1"
}

for i in $(seq "$start_port" "$end_port"); do
  check_ports "$i"
done

check_ports "$ceg01"
