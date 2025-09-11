#!/bin/bash
# This script is run after the container is created.
# It is used to install any additional dependencies or perform any setup tasks.

# Install Python 3.13 (latest version)
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.13 python3.13-dev python3.13-venv
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.13 1

sudo cp --force ./.devcontainer/welcome-message.txt /usr/local/etc/vscode-dev-containers/first-run-notice.txt