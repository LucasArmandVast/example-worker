#!/bin/bash
set -eo pipefail

rm -rf etc/supervisor/conf.d/*

mkdir -p /opt/workspace-internal/pytorch-model
mkdir -p /opt/supervisor-scripts

# ------------------------------------------------------------------------------
# Download model.py
# ------------------------------------------------------------------------------
curl -fsSL \
  https://raw.githubusercontent.com/LucasArmandVast/example-worker/pytorch/model.py \
  -o /opt/workspace-internal/pytorch-model/model.py

# ------------------------------------------------------------------------------
# Download model.sh
# ------------------------------------------------------------------------------
curl -fsSL \
  https://raw.githubusercontent.com/LucasArmandVast/example-worker/pytorch/model.sh \
  -o /opt/supervisor-scripts/model.sh

chmod +x /opt/supervisor-scripts/model.sh

# ------------------------------------------------------------------------------
# Add Supervisor application
# ------------------------------------------------------------------------------
cat > /etc/supervisor/conf.d/pytorch-model.conf << 'EOF'
# This program will always auto-start (no dependency on Portal config)
[program:pytorch-model]
environment=PROC_NAME="%(program_name)s"
command=/opt/supervisor-scripts/model.sh
autostart=true
autorestart=unexpected
exitcodes=0
startsecs=0
stopasgroup=true
killasgroup=true
stopsignal=TERM
stopwaitsecs=10
# This is necessary for Vast logging to work alongside the Portal logs
stdout_logfile=/dev/stdout
redirect_stderr=true
stdout_events_enabled=true
stdout_logfile_maxbytes=0
stdout_logfile_backups=0
EOF

# ------------------------------------------------------------------------------
# Reload Supervisor to pick up the new config
# ------------------------------------------------------------------------------
supervisorctl reread
supervisorctl update
