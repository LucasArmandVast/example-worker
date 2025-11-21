from vastai.serverless.remote.endpoint import Endpoint, benchmark, remote

@benchmark(
    endpoint_name="test-endpoint",
    dataset=[
        {"x": 1, "y": 2},   
        {"x": 3, "y": 4},
    ],
)
@remote(endpoint_name="test-endpoint")
async def remote_func_a(x: int, y: int):
    return x + y

@remote(endpoint_name="test-endpoint")
async def remote_func_b(x: int, y: int):
    return x * y

endpoint = Endpoint(
    name="test-endpoint"
)
endpoint.ready()