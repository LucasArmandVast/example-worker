from vastai_sdk import Worker, WorkerConfig, HandlerConfig
from aiohttp import web, ClientResponse
import json
import time

async def custom_response_handler(
    client_request: web.Request,
    model_response: ClientResponse
) -> web.Response:
    body_bytes = await model_response.read()
    body = json.loads(body_bytes.decode('utf-8'))
    
    # Add custom fields
    body["custom-field"] = "Custom field on response!"
    body["request-path"] = client_request.path
    
    print(f"Custom response handler called for {client_request.path}")
    
    # Return as JSON response
    return web.json_response(
        body,
        status=model_response.status
    )

def custom_request_parser(json_data: dict) -> dict:
    print(f"Custom request parser called")
    json_data["custom-field-1"] = "Custom field on request!"
    json_data['parsed_at'] = time.time()
    return json_data

# Create handler config
handler = HandlerConfig(
    route="/v1/completions",
    on_request=custom_request_parser,
    on_response=custom_response_handler,
    healthcheck="/health",
    benchmark_data=[
        {"prompt": "test prompt 1", "max_tokens": 50},
        {"prompt": "test prompt 2", "max_tokens": 100},
        {"prompt": "test prompt 3", "max_tokens": 150},
    ]
)

# Create worker config
worker_config = WorkerConfig(
    model_server_url="http://127.0.0.1",
    model_server_port=5001,
    model_log_file="/tmp/model.log",
    handlers=[handler],
    allow_parallel_requests=False,
    benchmark_route="/v1/completions"
)

Worker(worker_config).run()