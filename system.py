from copyreg import constructor
from typing import Tuple
from APIutils import *
from Schemas.SystemSchemas import *
from Schemas.ContractSchemas import Market
from Schemas.FleetSchemas import Shipyard,JumpGate,Construction,Good,ShipCargo

def listSystems(page: int=1, limit: int=10) -> Tuple[List[System], Meta]:
    querystring = {"page":page,"limit":limit}
    response =  requests.get(f"{url}/systems", headers=GetHeader(), params=querystring).json()
    systems=[System(i) for i in response["data"]]
    meta=Meta(response["meta"])

    return systems,meta

def getSystem(systemSymbol: str) -> System:
    response =  requests.get(f"{url}/systems/{systemSymbol}", headers=GetHeader()).json()

    return System(response["data"])

def listWaypointsInSystem(systemSymbol: str, traits: List[WaypointTraitSymbol]=None,type: WaypointType=None, page: int=1, limit: int=10) -> Tuple[List[Waypoint], Meta]:
    querystring = {"page":page,"limit":limit}
    if traits != None:
        querystring["traits"]=[i.value for i in traits]#filter by trait(s)
    if type != None:
        querystring["type"]=type.value#filter by type
    response =  requests.get(f"{url}/systems/{systemSymbol}/waypoints", headers=GetHeader(), params=querystring).json()
    waypoints=[Waypoint(i) for i in response["data"]]
    meta=Meta(response["meta"])

    return waypoints,meta

def getWaypoint(systemSymbol: str,waypointSymbol: str ) -> Waypoint:
    response =  requests.get(f"{url}/systems/{systemSymbol}/waypoints/{waypointSymbol}", headers=GetHeader()).json()
    return Waypoint(response["data"])

def getMarket(systemSymbol: str,waypointSymbol: str ) -> Market:
    response =  requests.get(f"{url}/systems/{systemSymbol}/waypoints/{waypointSymbol}/market", headers=GetHeader()).json()
    return Market(response["data"])

def getShipyard(systemSymbol: str,waypointSymbol: str ) -> Shipyard:
    response =  requests.get(f"{url}/systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard", headers=GetHeader()).json()
    return Shipyard(response["data"])
def getJumpGate(systemSymbol: str,waypointSymbol: str ) -> JumpGate:
    response =  requests.get(f"{url}/systems/{systemSymbol}/waypoints/{waypointSymbol}/jump-gate", headers=GetHeader()).json()
    return JumpGate(response["data"])
def getConstructionSite(systemSymbol: str,waypointSymbol: str ) -> Construction:
    response =  requests.get(f"{url}/systems/{systemSymbol}/waypoints/{waypointSymbol}/construction", headers=GetHeader()).json()
    return Construction(response["data"])

def supplyConstructionSite(token: str, systemSymbol: str, waypointSymbol: str,shipSymbol:str, tradeSymbol:str, good:Good) -> Tuple[Construction,ShipCargo]:

    payload = good.toJSON()
    payload["shipSymbol"]= shipSymbol
    payload["tradeSymbol"]= tradeSymbol

    response =  requests.post(f"{url}/systems/{systemSymbol}/waypoints/{waypointSymbol}/construction/supply", json=payload, headers=PostHeader(token)).json()

    construction=Construction(response["data"]["construction"])
    cargo=ShipCargo(response["data"]["cargo"])
    return construction,cargo
