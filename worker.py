from vastai import Worker
from vastai.serverless.server.templates.vllm import vLLM

print("configuring worker")
worker_config = vLLM()
print("starting worker")
Worker(worker_config).run()