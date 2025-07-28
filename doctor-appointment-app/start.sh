#!/bin/bash
cd /home/ubuntu/doctor-appointment-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
