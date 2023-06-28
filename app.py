from fastapi import FastAPI, Query

app = FastAPI()

networks = [
    # Network data entries...
]

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
            getattr(network, key) == value
            for key, value in locals().items()
            if key not in {"networks", "filtered_networks"} and value is not None
        )
    ]

    return {"networks": filtered_networks}
