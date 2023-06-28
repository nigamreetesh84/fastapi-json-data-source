import json
import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()

# Load data from JSON file
with open("networks.json") as file:
    networks = json.load(file)

@app.get("/networks")
async def get_networks(
    name: str = Query(None),
    ip: str = Query(None),
    cidr: int = Query(None),
    netmask: str = Query(None),
    side: str = Query(None),
    env: str = Query(None),
    location: str = Query(None),
    hosts: str = Query(None),
    id: int = Query(None),
    routers: str = Query(None),
):
    filtered_networks = [
        network
        for network in networks
        if all(
            network.get("name") == name,
            network.get("ip") == ip,
            network.get("cidr") == cidr,
            network.get("netmask") == netmask,
            network.get("side") == side,
            network.get("env") == env,
            network.get("location") == location,
            hosts in network.get("hosts", []),
            network.get("id") == id,
            routers in network.get("routers", [])
        )
    ]

    return {"networks": filtered_networks}
