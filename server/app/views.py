from aiohttp import web
import async_timeout
from agent_controller import agent_controller
import requests
import datetime
import secrets


async def invite(request):
    # Create Invitation
    # wait for the coroutine to finish
    with async_timeout.timeout(5):
        invite = await agent_controller.connections.create_invitation()
        connection_id = invite["connection_id"]
        invite_url = invite["invitation_url"]
        json_response = {"invite_url" : invite_url, "connection_id": connection_id}
        return web.json_response(json_response)


async def check_active(request: web.Request):

    connection_id = request.match_info["conn_id"]

    with async_timeout.timeout(2):

        connection = await agent_controller.connections.get_connection(connection_id)
        state = connection["state"]

        is_active = state == "active"

        json_response = {"active": is_active}

        return web.json_response(json_response)