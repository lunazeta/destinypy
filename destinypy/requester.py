from requests import request
from destinypy import exceptions

def GET(url: str, data={}, headers={}) -> dict:
    r = request("GET", url, data=data, headers=headers)
    if not r.ok:
        raise exceptions.APIError(r.json()["ErrorCode"], r.json()["Message"])
    return r.json()
    
def POST(url: str, data={}, headers={}) -> dict:
    r = request("POST", url, data=data, headers=headers)
    if not r.ok:
        raise exceptions.APIError(r.json()["ErrorCode"], r.json()["Message"])
    return r.json()