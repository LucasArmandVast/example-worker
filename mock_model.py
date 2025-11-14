from aiohttp import web
import json
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

async def handle_completions(request):
    """Mock completion endpoint"""
    data = await request.json()
    log.info(f"Model received request: {data}")
    
    # Simulate a response
    response = {
        "id": "cmpl-test",
        "object": "text_completion",
        "model": "test-model",
        "choices": [{
            "text": f"Response to: {data.get('prompt', 'no prompt')}",
            "index": 0,
            "finish_reason": "stop"
        }]
    }
    
    return web.json_response(response)

async def handle_health(request):
    """Health check endpoint"""
    return web.Response(text="OK", status=200)

app = web.Application()
app.add_routes([
    web.post('/v1/completions', handle_completions),
    web.get('/health', handle_health),
])

if __name__ == '__main__':
    print("Starting mock model server on port 5001...")
    web.run_app(app, host='127.0.0.1', port=5001)