from typing import Tuple
from APIutils import *
from Schemas.ContractSchemas import *
from Schemas.AgentSchemas import Agent
from Schemas.FleetSchemas import Good,ShipCargo


### 
# Contract Calls
###
def listContracts(token: str, page: int=1, limit: int=10) -> Tuple[List[Contract],Meta]:
    querystring = {"page":f"{page}","limit":f"{limit}"}
    #Return a paginated list of all your contracts.
    response = requests.get(f"{url}/my/contracts", headers=GetHeader(token), params=querystring).json()

    contracts=[Contract(i) for i in response["data"]]
    meta= Meta(response["meta"])
    return contracts,meta


def getContract(token,contractId)-> Contract:
    #Get the details of a contract by ID.
    response = requests.get(f"{url}/my/contracts/{contractId}", headers=GetHeader(token)).json()
    return Contract(response["data"])
    
def acceptContractById(token, contractId) -> Tuple[Agent,Contract]:
    '''
        Accept a contract by ID.
        You can only accept contracts that were offered to you, were not accepted yet, and whose deadlines has not passed yet
    '''

    response = requests.post(f"{url}/my/contracts/{contractId}/accept", headers=PostHeader(token)).json()

    agent=Agent(response["data"]["agent"])
    contract=Contract(response["data"]["contract"])

    return agent, contract

def deliverCargoToContract(token: str, contractId: str, shipSymbol: str, good:Good) -> Tuple[Contract,ShipCargo]:
    ''' 
        Deliver cargo to a contract.
        In order to use this API, a ship must be at the delivery location (denoted in the delivery terms as destinationSymbol of a contract) and must have a number of units of a good required by this contract in its cargo.
        Cargo that was delivered will be removed from the ship's cargo.
    '''
    payload = good.toJSON()
    payload["shipSymbol"]= shipSymbol

    response = requests.post(f"{url}/my/contracts/{contractId}/deliver", json=payload, headers=PostHeader(token)).json()

    contract=Contract(response["data"]["contract"])
    cargo = ShipCargo(response["data"]["cargo"])

    return contract,cargo


def fulfillContract(token: str, contractId: str) -> Tuple[Agent,Contract]:
    '''
        Fulfill a contract. Can only be used on contracts that have all of their delivery terms fulfilled.
    '''

    response = requests.post(f"{url}/my/contracts/{contractId}/fulfill", headers=PostHeader(token)).json()


    agent=Agent(response["data"]["agent"])
    contract=Contract(response["data"]["contract"])

    return agent, contract

