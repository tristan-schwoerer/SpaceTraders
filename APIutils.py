import requests
url = "https://api.spacetraders.io/v2"

class Meta():
    def __init__(self, JSON) -> None:
        total: int = JSON["total"]
        page: int = JSON["page"]
        limit: int = JSON["limit"]

def PostHeader(token=""):
    if token=="":
     return{
        "Content-Type": "application/json",
        "Accept": "application/json",
        }
    return     {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"}

def GetHeader(token=""):
    if token=="":
        return     {
        "Accept": "application/json"
        }
    return     {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"}
