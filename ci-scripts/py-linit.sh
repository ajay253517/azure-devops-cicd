#!/bin/bash 
echo "Installing py-lint"
pip install pylint Flask
echo "Running pylint"
pylint /tmp/app/app.py 
echo "----------------------------------"
echo "Execution completed calculating socre"