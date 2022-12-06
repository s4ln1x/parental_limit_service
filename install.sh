#!/usr/bin/env bash

# This is script MUST be run by root/sudo
if [ "$(id -u)" != "0" ]; then
    echo "Error: This script MUST be run by root/sudo"
    exit 1
fi

SCRIPT_PATH=$(dirname "$(realpath "${BASH_SOURCE[0]-$0}")")

# Using + as separator instead of /
sed -i "s+ExecStart\=+ExecStart\=${SCRIPT_PATH}/play.py /tmp/kid.txt+g " "${SCRIPT_PATH}"/parental-limit.service
sudo cp "${SCRIPT_PATH}"/parental-limit.service /etc/systemd/user
sudo systemctl enable --now parental-limit.service
