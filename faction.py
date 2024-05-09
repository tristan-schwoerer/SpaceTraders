from typing import Tuple
from APIutils import *
from Schemas.AgentSchemas import *

def listFactions(page: int=1, limit: int=10) -> Tuple[List[Faction], Meta]:
    '''
        Return a paginated list of all the factions in the game.
    '''
    querystring = {"page":page,"limit":limit}
    response =  requests.get(f"{url}/factions", headers=GetHeader(), params=querystring)
    factions=[Faction(i) for i in response["data"]]
    meta=Meta(response["meta"])

    return factions,meta

def getFaction(factionSymbol: str) -> Faction:
    '''
        View the details of a faction.
    '''
    response =  requests.get(f"{url}/factions/{factionSymbol}", headers=GetHeader()).json()

    return Faction(response["data"])
