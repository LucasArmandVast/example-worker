#!/bin/bash

utils=/opt/supervisor-scripts/utils
. "${utils}/logging.sh"
. "${utils}/environment.sh"

source /venv/main/bin/activate
exec pip install aiohttp
exec python3 /opt/workspace-internal/pytorch-model/model.py
