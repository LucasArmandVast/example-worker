FROM vastai/pytorch:cuda-12.8.1-auto

# Install additional Python packages
RUN . /venv/main/bin/activate && \
    pip install aiohttp

RUN rm -rf /etc/supervisor/conf.d/*