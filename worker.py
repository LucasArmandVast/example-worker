from vastai import Worker
from vastai.serverless.server.templates import vLLM

worker_config = vLLM()
Worker(worker_config).run()