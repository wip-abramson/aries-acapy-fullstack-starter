# Aries Full Stack Starter 

## A full stack SSI application developed using ACA-Py, Python and React

You must have docker installed to run this project.

To start run `./manage up`

Client: [http://localhost:3000](http://localhost:3000)
Server: [http://localhost:8000/](http://localhost:8000/)
Agent: [http://localhost:8011/api/doc](http://localhost:8011/api/doc)


## Services

See docker-compose.yml

### Agent

An ACA-Py agent configured using the startup.sh script. Agent storage is made persistent using docker-volumes.

### Server

An aiohttp server that receives requests from the frontend and uses the [aries-basic-controller](https://github.com/OpenMined/PyDentity/tree/master/libs/aries-basic-controller) library to send a receive communication from the agent.

On startup the server checks if the agent has a public DID on the ledger, if not one is written to it (in agent_controller.py). This is where you can extend the code to include specific credential schema or definitions. Just remember you will only need to write them once, so your code should check if the agent has already written them for their public DID as state is persisted.

### Client

A React Frontend created using the create-react-app template, this basic template includes a QrCode for an invitation which can be scanned by any mobile agent on the Sovrin StagingNet. Once the connection moves to active a default page is shown with some pointers for how to extend this code.