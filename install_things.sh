#!/bin/bash
curl -sSL https://get.docker.com/ | sh
apt-get update -y
apt-get install python-pip -y
pip install docker-compose
cp systemd/* /etc/systemd/system
