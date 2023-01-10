from requests import request

class APIError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def GET(url: str, data={}, headers={}) -> dict:
    r = request("GET", url, data=data, headers=headers)
    if not r.ok:
        if r.json()["ErrorStatus"] == "UserCannotFindRequestedUser":
            raise LookupError(r.json()["Message"])
        else:
            raise APIError("Request failed")
    return r.json()
    
def POST(url: str, data={}, headers={}) -> dict:
    r = request("POST", url, data=data, headers=headers)
    if not r.ok:
        if r.json()["ErrorStatus"] == "UserCannotFindRequestedUser":
            raise LookupError(r.json()["Message"])
        else:
            raise APIError("Request failed")
    return r.json()