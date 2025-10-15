from vastai_sdk import Worker, vLLM
worker_config = vLLM()
Worker(worker_config).run()