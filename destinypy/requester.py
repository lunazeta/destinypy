from requests import request

def GET(url: str, data={}, headers={}) -> dict:
    r = request("GET", url, data=data, headers=headers)
    if not r.ok:
        if r.json()["ErrorStatus"] == "UserCannotFindRequestedUser":
            raise LookupError(r.json()["Message"])
        else:
            raise ConnectionError("Request failed")
    return r.json()