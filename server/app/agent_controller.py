
import os
import requests
import logging
import json
import config
import time
import asyncio
from aries_basic_controller import AriesAgentController


logger = logging.getLogger("agent_controller")


WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
WEBHOOK_PORT = os.getenv('WEBHOOK_PORT')
WEBHOOK_BASE = os.getenv('WEBHOOK_BASE')
ADMIN_URL = os.getenv('ADMIN_URL')
API_KEY = os.getenv('API_KEY')

print(WEBHOOK_HOST)
print(WEBHOOK_PORT)
print(WEBHOOK_BASE)

logger.info(f"Initialising Agent. Webhook URL {WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_BASE}. ADMIN_URL - {ADMIN_URL}")

agent_controller = AriesAgentController(webhook_host=WEBHOOK_HOST, webhook_port=WEBHOOK_PORT,
                                       webhook_base="", admin_url=ADMIN_URL, api_key=API_KEY)



def cred_handler(payload):
    print("Handle Credentials")
    exchange_id = payload['credential_exchange_id']
    state = payload['state']
    role = payload['role']
    # attributes = payload['credential_proposal_dict']['credential_proposal']['attributes']
    logger.debug(f"Credential exchange {exchange_id}, role: {role}, state: {state}")
    # print(f"Offering: {attributes}")


cred_listener = {
    "topic": "issue_credential",
    "handler": cred_handler
}




def connections_handler(payload):
    global STATE
    connection_id = payload["connection_id"]
    logger.debug("Connection message", payload, connection_id)
    STATE = payload['state']
    if STATE == "response":

        # Ensures connections moved to active
        loop = asyncio.get_event_loop()
        loop.create_task(agent_controller.messaging.trust_ping(connection_id, 'hello!'))
        time.sleep(3)
        loop.create_task(agent_controller.messaging.trust_ping(connection_id, 'hello!'))


connection_listener = {
    "handler": connections_handler,
    "topic": "connections"
}



async def initialise():
    await agent_controller.listen_webhooks()

    agent_controller.register_listeners([cred_listener, connection_listener], defaults=True)

    is_alive = False
    while not is_alive:
        try:
            await agent_controller.server.get_status()
            is_alive = True
            logger.info("Agent Active")
        except:

            time.sleep(5)

    response = await agent_controller.wallet.get_public_did()

    if not response['result']:
        did = await write_public_did()
        logger.info(f"Public DID {did} written to the ledger")


    ## Write Cred Def and Schema to ledger
    # response = await agent_controller.definitions.write_cred_def(config.schema_id)
    #
    # config.cred_def_id = response["credential_definition_id"]
    # logger.info(f"Credential Definition {config.cred_def_id} for schema {config.schema_id}")


async def write_public_did():
    # generate new DID
    response = await agent_controller.wallet.create_did()

    did_object = response['result']
    did = did_object["did"]
    logger.debug("New DID", did)
    # write new DID to Sovrin Stagingnet

    url = 'https://selfserve.sovrin.org/nym'

    payload = {"network": "stagingnet", "did": did_object["did"], "verkey": did_object["verkey"], "paymentaddr": ""}

    # Adding empty header as parameters are being sent in payload
    headers = {}

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    if r.status_code != 200:
        logger.error("Unable to write DID to StagingNet")
        raise Exception

    response = await agent_controller.ledger.get_taa()
    taa = response['result']['taa_record']
    taa['mechanism'] = "service_agreement"

    await agent_controller.ledger.accept_taa(taa)

    await agent_controller.wallet.assign_public_did(did)

    return did_object["did"]