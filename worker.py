from vastai_sdk import Worker, vLLM
import logging
import os

# This is all you need for logging - same as before
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s[%(levelname)-5s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


worker_config = vLLM()
Worker(worker_config).run()