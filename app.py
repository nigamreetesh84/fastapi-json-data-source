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
    results = []
    for device in devices:
        match_criteria = []
        if primaryName:
            match_criteria.append(device["primaryName"] == primaryName)
        if ownerEonid:
            match_criteria.append(device["system"]["ownerEonid"] == ownerEonid)
        if ip:
            match_criteria.append(
                any(
                    assignment["ip"] == ip
                    for interface in device["hardware"]["interfaces"]
                    for assignment in interface["addressAssignments"]
                )
            )
        if len(match_criteria) == 0 or all(match_criteria):
            results.append(device)

    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
