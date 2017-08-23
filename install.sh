#!/bin/bash
#set up required environment for python-twitter development
activate_venv()
{
  echo "activating venv"
  source .pt-venv/bin/activate
  echo "venv activated"
}

python3 -m venv .pt-venv
activate_venv
echo "installing requirements"
pip install -r requirements.txt
echo "requirements installed"
echo "remember to activate the virtual environment"
