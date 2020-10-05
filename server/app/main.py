from aiohttp import web
from routes import setup_routes
from agent_controller import initialise
import asyncio
import aiohttp_cors

loop = asyncio.get_event_loop()
loop.run_until_complete(initialise())

app = web.Application()
setup_routes(app)

# Configure default CORS settings.
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
})

# Configure CORS on all routes.
for route in list(app.router.routes()):
    cors.add(route)

web.run_app(app, host='0.0.0.0', port=8000)