import json
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
            (
                name is None or network.get("name") == name,
                ip is None or network.get("ip") == ip,
                cidr is None or network.get("cidr") == cidr,
                netmask is None or network.get("netmask") == netmask,
                side is None or network.get("side") == side,
                env is None or network.get("env") == env,
                location is None or network.get("location") == location,
                hosts is None or hosts in network.get("hosts", []),
                id is None or network.get("id") == id,
                routers is None or routers in network.get("routers", []),
            )
        )
    ]

    return {"networks": filtered_networks}
