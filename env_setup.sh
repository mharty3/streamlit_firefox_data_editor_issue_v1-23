#!/usr/bin/env bash
python -m venv venv_streamlit_version_1-22
venv_streamlit_version_1-22/bin/python -m pip install --upgrade pip
venv_streamlit_version_1-22/bin/python -m pip install -r requirements_v1-22.txt

python -m venv venv_streamlit_version_1-23
venv_streamlit_version_1-23/bin/python -m pip install --upgrade pip
venv_streamlit_version_1-23/bin/python -m pip install -r requirements_v1-23.txt