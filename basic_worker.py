from vastai_sdk import Worker, WorkerConfig, HandlerConfig
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

handler_config = HandlerConfig(
    route="/v1/completions"
)

worker_config = WorkerConfig(
    model_server_port=18000,
    model_log_file="/var/log/portal/vllm.log",
    handlers=[handler_config]
)

Worker(worker_config).run()