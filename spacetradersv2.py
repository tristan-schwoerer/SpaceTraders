from APIutils import *
from agent import *
from fleet import listShips, shipRefine
from game import *

email="tristan@5schwoerer.de"
player_symbol="tristan9497"
token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiVFJJU1RBTjk0OTciLCJ2ZXJzaW9uIjoidjIuMi4wIiwicmVzZXRfZGF0ZSI6IjIwMjQtMDQtMjgiLCJpYXQiOjE3MTUwMjQ1OTEsInN1YiI6ImFnZW50LXRva2VuIn0.CGoeDBoAL9YD7fIr1kDdaOXau8OID7NDx-XHLaVSLSgpoarcci6DlgqytPMonB6jDjEB6ORLzt-E43wvI8lqYX0-s4XLZVgcFhAaRTqrZAgzuG9BWmPDacRmPzawLjpof8OmiUFzyFr8HOerhFOTC9naHVtCQmWZFI2_UFnR8trvfn4tUHlHFJaSAp6kXTlyWzmOiLNZhdF6VEY6RdrWMnCh-uTpcaw6Qyycph7T4Zdw0Y121oNMFZmWdX0FUkWfM3s-fF67AMPSjakzV4GcuCNQBYuKuFPCS-QWPICp_TRUP6aKZJAl32z92OcuPmNZO5tXFqKyF2fvIismsGKhNw"









# def firstMission():
#     status=getStatus().json()["status"]
#     if status=="SpaceTraders is currently online and available to play":
#         Agent=getAgent(token)
#         ships=listShips(token,page=2,limit=2).json()["data"]

#         print(ships)
#         # scanWaypoints
#         # response=registerPlayer(str(Faction.COSMIC.value),"Tristan9497","tristan@5schwoerer.de")
if __name__=="__main__":
    # print(registerPlayer(FactionSymbol.AEGIS.value,"Tristan9497","tristan@5schwoerer.de").json())
    # print(getStatus().json())
    print(getAgent(token).symbol)
    ships, meta=listShips(token)
    print(ships[0].symbol)
    
    # print(getPublicAgent("TRISTAN9497").accountID)