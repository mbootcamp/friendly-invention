#!/bin/bash
curl -sSL https://get.docker.com/ | sudo sh
sudo apt-get update -y
sudo apt-get install python-pip -y
sudo pip install docker-compose
sudo cp systemd/* /etc/systemd/system
sudo usermod -aG docker $USER
newgrp docker
