from typing import Optional, List
from fastapi import FastAPI, Query
import json


app = FastAPI()

DATA_DUMP_FILE = "data_dump.json"

with open(DATA_DUMP_FILE) as fd:
    devices = json.load(fd)


@app.get("/devices")
async def get_devices(
    primaryName: Optional[str] = Query(None),
    ownerEonid: Optional[int] = Query(None),
    ip: Optional[str] = Query(None),
):
    if not primaryName and not ownerEonid and not ip:
        return devices

    results = []
    for device in devices:
        if primaryName and device["primaryName"] == primaryName:
            results.append(device)
        elif ownerEonid and device["system"]["ownerEonid"] == ownerEonid:
            results.append(device)
        elif ip:
            for interface in device["hardware"]["interfaces"]:
                for assignment in interface["addressAssignments"]:
                    if assignment["ip"] == ip:
                        results.append(device)
                        break

    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
