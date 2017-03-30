#!/bin/bash
curl -sSL https://get.docker.com/ | sh
apt-get update
apt-get install python-pip
pip install docker-compose
#cp systemd/* /etc/systemd/system
