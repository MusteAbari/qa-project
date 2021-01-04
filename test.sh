#!/bin/bash
cd /opt/qa-project
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov

pytest --cov=application --cov-report xml --cov-report