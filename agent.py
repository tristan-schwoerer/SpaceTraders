from typing import Tuple
from APIutils import *
from Schemas.AgentSchemas import *

### 
# Agents Calls
###
def getAgent(token):
    #fetches own agent
    response=requests.get(f"{url}/my/agent", headers=GetHeader(token)).json()
    return Agent(response["data"])

def listPublicAgents(page: int=1, limit: int=10) -> Tuple[List[Agent],Meta]:
    querystring = {"page":f"{page}","limit":f"{limit}"}
    response=requests.get(f"{url}/agents", headers=GetHeader(), params=querystring).json()
    agents=[Agent(i) for i in response["data"]]

    meta=Meta(response["meta"])
    return agents,meta

def getPublicAgent(symbol):
    response=requests.get(f"{url}/agents/{symbol}", headers=GetHeader()).json()
    return Agent(response["data"])
