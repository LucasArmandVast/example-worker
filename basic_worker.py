from vastai import Worker, WorkerConfig, HandlerConfig, BenchmarkConfig

handler_config = HandlerConfig(
    route="/v1/completions"
)

worker_config = WorkerConfig(
    model_server_port=18000,
    model_log_file="/var/model/out.log",
    handlers=[
        HandlerConfig(
            route="/my/route",
            benchmark_config=BenchmarkConfig(
                dataset=[
                    "some",
                    "example",
                ]
            )
        )
    ]
)

Worker(worker_config).run_sync()