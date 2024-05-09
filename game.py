from APIutils import *
'''General API Calls'''

def getStatus(token:str=""):
    '''
        Get status with or without auth
    '''
    return requests.get(f"{url}/", headers=GetHeader(token))

def registerPlayer(faction: str, symbol: str, email: str):
    payload = {
    "faction": faction,
    "symbol": symbol,
    "email": email
    }
    return requests.post(f"{url}/register", json=payload, headers=PostHeader())
