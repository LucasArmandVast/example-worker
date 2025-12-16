FROM vastai/pytorch:cuda-12.8.1-auto

# Install additional Python packages
RUN . /venv/main/bin/activate && \
    pip install aiohttp

RUN mkdir -p /opt/workspace-internal/pytorch-model

COPY model.py /opt/workspace-internal/pytorch-model/

RUN rm -rf /etc/supervisor/conf.d/*
COPY model.conf /etc/supervisor/conf.d/
COPY model.sh /opt/supervisor-scripts/
RUN chmod +x /opt/supervisor-scripts/model.sh