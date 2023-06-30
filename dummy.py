from fastapi import FastAPI, Query

app = FastAPI()

devices = {
    "primaryName": "hn02pd1r05.vhub.halsey.ms.com",
    "hardware": {
        "hardwareType": "NETWORK_DEVICE",
        "label": "hn@2pd1r05",
        "model": {
            "name": "generic",
            "vendor": "arista",
            "modelType": "switch"
        },
        "location": {
            "name": "hn.02.ac.21",
            "locationType": "rack",
            "fullname": "hn.02.ac.21",
            "row": "ac",
            "col": 21
        },
        "interfaces": [
            {
                "device": "lo10",
                "bootable": False,
                "interfaceType": "loopback",
                "addressAssignments": [
                    {
                        "assignmentType": "STANDARD",
                        "ip": "12.23.234.12",
                        "fqdn": ["abc@gmail.com", "abcd@gmail.com"]
                    }
                ]
            }
        ]
    },
    "system": {
        "domain": {
            "name": "netinfra",
            "type": "DOMAIN",
            "allowManage": True,
            "trackedBranch": "prod"
        },
        "status": "build",
        "personality": {
            "name": "generic",
            "archetype": {
                "name": "netinfra",
                "compileable": False
            },
            "ownerEonid": 48510,
            "configOverride": False,
            "clusterRequired": False,
            "hostEnvironment": "prod"
        },
        "operatingSystem": {
            "archetype": {
                "name": "netinfra",
                "compileable": False
            },
            "name": "generic",
            "version": "generic",
            "lifecycle": "PRODUCTION"
        },
        "ownerEonid": 48510
    }
}


@app.get("/devices")
async def get_devices(search_key: str = Query(None)):
    if search_key is None:
        return devices
    else:
        results = {}
        for key, value in devices.items():
            if search_key.lower() in key.lower():
                results[key] = value
        return results

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
