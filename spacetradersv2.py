from APIutils import *
from Schemas.ContractSchemas import Contract
from agent import *
from contract import acceptContractById, listContracts
from fleet import listShips, shipRefine
from game import *
from system import *

from pprint import pprint
email="tristan@5schwoerer.de"
player_symbol="tristan9497"
token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiVFJJU1RBTjk0OTgiLCJ2ZXJzaW9uIjoidjIuMi4wIiwicmVzZXRfZGF0ZSI6IjIwMjQtMDQtMjgiLCJpYXQiOjE3MTUyNjkzNjIsInN1YiI6ImFnZW50LXRva2VuIn0.C6tqxSHHiAF7E8THdh8lBHU-LIjB-y0TR8bPm6lLcVsEp6xtkUb5bmFPfU9jvmcj8gIo31-p02UZgiDO0K69bNkCUePyZN0oObCcCWGTBkDaBF1FuQKbD_isgux8G5t5DT2TNZRRObbef474zaxfDPT_00Mg9GW2y5NYYxXVi9qs2Kjdj3uIexRkq6swXUkzAVFgAyPA8tEoja-Y2kE3Wj_SteciSRLWificrqaCO_QsnUcE26fbzENn9pdkCD5eAlsTRJyI3S-Gavy2f3DYa_0eJzt5M7stsDQO-6p0xYq0O_0XHTcWpvLeQ4RbP2pXk_iMIi6NO-zG7sSD9z7_MQ"








def firstmission():

    contracts,meta =listContracts(token)
    pprint(vars(contracts[0]))
    agent, contract= acceptContractById(token,contracts[0].id)
    wp,_=listWaypointsInSystem("X1-HF96",[WaypointTraitSymbol.SHIPYARD])
    shipyard=getShipyard("X1-HF96","X1-HF96-C43")
    pprint(vars(agent))
    print("--------------------------------------")
    pprint(vars(contract))

if __name__=="__main__":
    # print(registerPlayer(FactionSymbol.AEGIS.value,"Tristan9498","tristan@5schwoerer.de").json())
    # print(getStatus().json())
    #print(listSystems())
    # sys,_= listSystems(20,20)
    

    # pprint(vars(getAgent(token)))
    shipyard=getShipyard("X1-HF96","X1-HF96-C43")

    pprint(vars(shipyard))
    # waypoints,_=listWaypointsInSystem(":systemSymbol",[WaypointTraitSymbol.SHIPYARD])

    # pprint(vars(waypoints[0]))
    