#!/bin/bash

# Exit on error
set -e

echo "Updating system..."
sudo apt update

echo "Installing Python, pip, and venv..."
sudo apt install -y python3 python3-pip python3-venv

echo "Creating and activating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Installing Airflow (latest stable)..."
pip install apache-airflow

echo "Setting AIRFLOW_HOME and initializing Airflow DB..."
export AIRFLOW_HOME=$(pwd)/airflow
mkdir -p "$AIRFLOW_HOME"
airflow db init

echo "Creating Airflow admin user..."
airflow users create --username sks --firstname Shivam --lastname Gupta --role Admin --email sks.shivam339@zohomail.in --password sks339@zoho

echo "Setup complete!"
echo "To start Airflow webserver, run: source .venv/bin/activate && export AIRFLOW_HOME=$(pwd)/airflow && airflow webserver -p 8085"
echo "To start Airflow scheduler, run: source .venv/bin/activate && export AIRFLOW_HOME=$(pwd)/airflow && airflow scheduler"
