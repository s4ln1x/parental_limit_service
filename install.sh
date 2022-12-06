#!/usr/bin/env bash

# This is script MUST be run by root/sudo
if [ "$(id -u)" != "0" ]; then
    echo "Error: This script MUST be run by root/sudo"
    exit 1
fi

SCRIPT_PATH=$(dirname "$(realpath "${BASH_SOURCE[0]-$0}")")
sudo cp "${SCRIPT_PATH}"/parental-limit.service /etc/systemd/system/
sudo cp "${SCRIPT_PATH}"/play.py /usr/local/bin/
sudo systemctl daemon-reload
sudo systemctl enable --now parental-limit.service
