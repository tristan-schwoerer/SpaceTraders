from typing import Tuple
from APIutils import *
from Schemas.ContractSchemas import Contract, MarketTransaction, RepairTransaction, ScrapTransaction, TradeGood
from Schemas.FleetSchemas import *

### 
# Fleet Calls
###
def listShips(token: str,page: int=1, limit: int=10) -> Tuple[List[Ship],Meta]:
    querystring = {"page":page,"limit":limit}
    response = requests.get(f"{url}/my/ships", headers=GetHeader(token), params=querystring).json()
    # print(response["data"])
    ships=[Ship(i) for i in response["data"]]
    meta=Meta(response["meta"])
    return ships,meta

def purchaseShip(token: str,shipType:str="SHIP_PROBE", waypointSymbol:str="string") -> Tuple[Agent,Ship,ShipyardTransaction]:
    payload = {
        "shipType": ShipType(shipType).value,
        "waypointSymbol": waypointSymbol
    }
    response = requests.post(f"{url}/my/ships", json=payload, headers=PostHeader(token)).json()
    agent=Agent(response["data"]["agent"])
    ship=Ship(response["data"]["ship"])
    transaction=ShipyardTransaction(response["data"]["transaction"])

    return agent,ship,transaction

def getShip(token:str,shipSymbol:str) -> Ship:
    '''Get Ship details'''
    response = requests.get(F"{url}/my/ships/{shipSymbol}", headers=GetHeader(token)).json()
    return Ship(response["data"])

def getShipCargo(token:str, shipSymbol:str)-> ShipCargo:
    response = requests.get(F"{url}/my/ships/{shipSymbol}/cargo", headers=GetHeader(token)).json()
    return ShipCargo(response["data"])

def orbitShip(token:str, shipSymbol:str)-> ShipNav:
    response = requests.post(f"{url}/my/ships/{shipSymbol}/orbit", headers=PostHeader(token)).json()
    return ShipNav(response["data"]["nav"])

def shipRefine(token:str,shipSymbol:str,productionType:str) -> Tuple[ShipCargo,Cooldown,Good,Good]:
    """

    :returns: 
        - ShipCargo
        - Cooldown
        - ProducedGoods
        - ConsumedGoods
    """
    payload = { "produce": productionType }
    
    response = requests.post(f"{url}/my/ships/{shipSymbol}/refine", json=payload, headers=PostHeader(token)).json()
    shipcargo=ShipCargo(response["data"]["cargo"])
    cooldown=Cooldown(response["data"]["cooldown"])
    produced=Good(response["data"]["produced"])
    consumed=Good(response["data"]["consumed"])

    return shipcargo,cooldown,produced,consumed

def createChart(token:str,shipSymbol:str) -> Tuple[Chart,Waypoint]:

    response = requests.post(f"{url}/my/ships/{shipSymbol}/chart", headers=PostHeader(token)).json()
    chart=ShipCargo(response["data"]["chart"])
    waypoint=Waypoint(response["data"]["waypoint"])

    return chart,waypoint

def getShipCooldown(token:str, shipSymbol:str)->Cooldown:

    response = requests.get(f"{url}/my/ships/{shipSymbol}/cooldown", headers=GetHeader(token)).json()

    return Cooldown(response["data"])

def dockShip(token:str, shipSymbol:str) -> ShipNav:

    response = requests.post(f"{url}/my/ships/{shipSymbol}/dock", headers=PostHeader(token)).json()
    return ShipNav(response["data"]["nav"])

def createSurvey(token:str,shipSymbol:str) -> Tuple[Cooldown,List[Survey]]:

    response = requests.post(f"{url}/my/ships/{shipSymbol}/survey", headers=PostHeader(token)).json()


    cooldown=Cooldown(response["data"]["cooldown"])
    surveys=[Survey(i) for i in response["data"]["surveys"]]

    return cooldown,surveys

def extractResources(token:str,shipSymbol:str,survey:Survey) -> Tuple[Cooldown,Extraction,ShipCargo,List[ShipConditionEvent]]:
    """
    Might be a deprecated endpoint
    """
    payload = {"survey": survey.toJSON()}
    response = requests.post(f"{url}/my/ships/{shipSymbol}/extract", json=payload,headers=PostHeader(token)).json()

    cooldown=Cooldown(response["data"]["cooldown"])
    extraction=Extraction(response["data"]["extraction"])
    cargo=ShipCargo(response["data"]["cargo"])
    events=[ShipConditionEvent(i) for i in response["data"]["events"]]

    return cooldown,extraction,cargo,events


def syphonResource(token:str,shipSymbol:str) -> Tuple[Cooldown,Syphon,ShipCargo,List[ShipConditionEvent]]:

    response = requests.post(f"{url}/my/ships/{shipSymbol}/siphon", headers=PostHeader(token)).json()

    cooldown=Cooldown(response["data"]["cooldown"])
    syphon=Extraction(response["data"]["syphon"])
    cargo=ShipCargo(response["data"]["cargo"])
    events=[ShipConditionEvent(i) for i in response["data"]["events"]]

    return cooldown,syphon,cargo,events

def extractResourcesWithSurvey(token: str,shipSymbol: str, survey: Survey) -> Tuple[Cooldown,Extraction,ShipCargo,List[ShipConditionEvent]]:

    payload = survey.toJSON()
    response = requests.post(f"{url}/my/ships/{shipSymbol}/extract/survey", json=payload,headers=PostHeader(token)).json()

    cooldown=Cooldown(response["data"]["cooldown"])
    extraction=Extraction(response["data"]["extraction"])
    cargo=ShipCargo(response["data"]["cargo"])
    events=[ShipConditionEvent(i) for i in response["data"]["events"]]

    return cooldown,extraction,cargo,events

def jettisonCargo(token:str, shipSymbol: str, good:Good) -> ShipCargo:

    payload = good.toJSON()

    response = requests.post(f"{url}/my/ships/{shipSymbol}/jettison", json=payload,headers=PostHeader(token)).json()
    
    return ShipCargo(response["data"]["cargo"])

def jumpShip(token:str, shipSymbol: str, waypointSymbol:str) -> Tuple[ShipNav,Cooldown,MarketTransaction,Agent]:

    payload = { "waypointSymbol": waypointSymbol }

    response = requests.post(f"{url}/my/ships/{shipSymbol}/jump", json=payload,headers=PostHeader(token)).json()

    cooldown=Cooldown(response["data"]["cooldown"])
    shipnav=ShipNav(response["data"]["nav"])
    transaction=MarketTransaction(response["data"]["transaction"])
    agent=MarketTransaction(response["data"]["agent"])

    return shipnav,cooldown,transaction,agent

def navigateShip(token:str, shipSymbol: str, waypointSymbol:str) -> Tuple[ShipFuel,ShipNav,List[ShipConditionEvent]]:
    payload = { "waypointSymbol": waypointSymbol }

    response = requests.post(f"{url}/my/ships/{shipSymbol}/navigate", json=payload,headers=PostHeader(token)).json()    
    fuel=ShipFuel(response["data"]["fuel"])
    shipnav=ShipNav(response["data"]["nav"])
    events=[ShipConditionEvent(i) for i in response["data"]["events"]]

    return fuel,shipnav,events

def patchShipNav(token: str, shipSymbol: str, flightMode: ShipFlightMode) -> ShipNav:

    payload = { "flightMode": flightMode.value }

    response = requests.patch(f"{url}/my/ships/{shipSymbol}/nav", json=payload, headers=PostHeader(token)).json()

    return ShipNav(response["data"])

def getShipNav(token: str, shipSymbol: str) -> ShipNav:

    response = requests.get(f"{url}/my/ships/{shipSymbol}/nav", headers=GetHeader(token)).json()

    return ShipNav(response["data"])

def warpShip(token:str,shipSymbol:str,waypoint:str) -> Tuple[ShipFuel,ShipNav]:

    payload = { "waypointSymbol": waypoint }

    response = requests.post(f"{url}/my/ships/{shipSymbol}/warp", json=payload, headers=PostHeader(token)).json()

    fuel = ShipFuel(response["data"]["fuel"])
    nav = ShipNav(response["data"]["nav"])

    return fuel,nav


def sellCargo(token: str, shipSymbol: str, good: Good) -> Tuple[Agent,ShipCargo,MarketTransaction]:
    payload = good.toJSON()
    response = requests.post(f"{url}/my/ships/{shipSymbol}/sell", json=payload, headers=PostHeader(token)).json()
    agent=Agent(response["data"]["agent"])
    cargo=ShipCargo(response["data"]["cargo"])
    transaction=MarketTransaction(response["data"]["transaction"])

    return agent,cargo,transaction

def scanSystems(token: str, shipSymbol: str) -> Tuple[Cooldown,List[ScannedSystem]]:
    response = requests.post(f"{url}/my/ships/{shipSymbol}/scan/systems", headers=PostHeader(token)).json()

    cooldown=Cooldown(response["data"]["cooldown"])    
    systems=[ScannedSystem(i) for i in response["data"]["systems"]]

    return cooldown,systems
  
def scanWaypoints(token: str, shipSymbol: str) -> Tuple[Cooldown,List[ScannedWaypoint]]:
    response = requests.post(f"{url}/my/ships/{shipSymbol}/scan/waypoints", headers=PostHeader(token)).json()
    cooldown=Cooldown(response["data"]["cooldown"])    
    waypoints=[ScannedWaypoint(i) for i in response["data"]["waypoints"]]

    return cooldown,waypoints
    
def scanShips(token: str, shipSymbol: str) -> Tuple[Cooldown,List[ScannedShip]]:
    response = requests.post(f"{url}/my/ships/{shipSymbol}/scan/ships", headers=PostHeader(token)).json()
    cooldown=Cooldown(response["data"]["cooldown"])    
    ships=[ScannedShip(i) for i in response["data"]["ships"]]

    return cooldown,ships

def refuelShip(token: str, shipSymbol: str, units:int, fromCargo:bool=False) -> Tuple[Agent,ShipFuel,MarketTransaction]:
    payload = {
        "units": str(units),
        "fromCargo": fromCargo
    }
    response = requests.post(f"{url}/my/ships/{shipSymbol}/refuel", json=payload, headers=PostHeader(token)).json()
    agent=Agent(response["data"]["agent"]) 
    fuel=ShipFuel(response["data"]["fuel"]) 
    transaction=MarketTransaction(response["data"]["cooldtransactionown"]) 
    return agent,fuel,transaction

def purchaseCargo(token: str, shipSymbol: str, good: Good) -> Tuple[Agent,ShipFuel,MarketTransaction]:
    payload = good.toJSON()

    response = requests.post(f"{url}/my/ships/{shipSymbol}/purchase", json=payload, headers=PostHeader(token)).json()
    agent=Agent(response["data"]["agent"]) 
    cargo=ShipCargo(response["data"]["fuel"]) 
    transaction=MarketTransaction(response["data"]["transaction"]) 

    return agent,cargo,transaction

def transferCargo(token: str, shipSymbol: str, good: Good, shipToTransferTo: str) -> ShipCargo:
    payload = good.toJSON()
    payload["shipSymbol"]=shipToTransferTo

    response = requests.post(f"{url}/my/ships/{shipSymbol}/transfer", json=payload, headers=PostHeader(token)).json()

    return ShipCargo(response["data"]["cargo"])

def negotiateNewContract(token: str, shipSymbol: str) -> Contract:

    response = requests.post(f"{url}/my/ships/{shipSymbol}/negotiate/contract", headers=PostHeader(token)).json()

    return Contract(response["data"]["contract"])

def getMounts(token: str, shipSymbol: str) -> List[ShipMount]:
    response = requests.get(f"{url}/my/ships/{shipSymbol}/mounts", headers=GetHeader(token)).json()

    return [ShipMount(i) for i in response["data"]]

def installMounts(token: str, shipSymbol: str, mountSymbol: str ) -> Tuple[Agent,List[ShipMount],ShipCargo,ShipModificationTransaction]:
    payload = { "symbol": mountSymbol}
    response = requests.post(f"{url}/my/ships/{shipSymbol}/mounts/install", json=payload, headers=PostHeader(token)).json()

    agent=Agent(response["data"]["agent"]) 
    mounts = [ShipMount(i) for i in response["data"]["mounts"]]
    cargo=ShipCargo(response["data"]["cargo"]) 
    transaction=ShipModificationTransaction(response["data"]["transaction"]) 

    return agent,mounts,cargo,transaction

def removeMounts(token: str, shipSymbol: str, mountSymbol: str ) -> Tuple[Agent,List[ShipMount],ShipCargo,ShipModificationTransaction]:
    payload = { "symbol": mountSymbol}
    response = requests.post(f"{url}/my/ships/{shipSymbol}/mounts/remove", json=payload, headers=PostHeader(token)).json()

    agent=Agent(response["data"]["agent"]) 
    mounts = [ShipMount(i) for i in response["data"]["mounts"]]
    cargo=ShipCargo(response["data"]["cargo"]) 
    transaction=ShipModificationTransaction(response["data"]["transaction"]) 
    return agent,mounts,cargo,transaction

def getScrapShip(token: str, shipSymbol: str) -> ScrapTransaction:
    response = requests.get(f"{url}/my/ships/{shipSymbol}/scrap", headers=GetHeader(token)).json()

    return ScrapTransaction(response["data"]["transaction"]) 

def scrapShip(token: str, shipSymbol: str) -> Tuple[Agent,ScrapTransaction]:
    response = requests.post(f"{url}/my/ships/{shipSymbol}/scrap", headers=PostHeader(token)).json()

    agent = Agent(response["data"]["agent"]) 
    transaction= ScrapTransaction(response["data"]["transaction"]) 
    return agent,transaction

def getRepairShip(token: str, shipSymbol: str) -> RepairTransaction:
    response = requests.get(f"{url}/my/ships/{shipSymbol}/repair", headers=GetHeader(token)).json()

    return RepairTransaction(response["data"]["transaction"]) 

def repairShip(token: str, shipSymbol: str) -> Tuple[Agent,RepairTransaction]:
    response = requests.post(f"{url}/my/ships/{shipSymbol}/repair", headers=PostHeader(token)).json()

    agent = Agent(response["data"]["agent"]) 
    transaction= RepairTransaction(response["data"]["transaction"]) 

    return agent,transaction

