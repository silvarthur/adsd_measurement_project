#!/bin/bash
apt-get update
apt-get install -y python-pip python-dev
python3 -m venv dev-env
source dev-env/bin/activate
pip install -r requirements.txt