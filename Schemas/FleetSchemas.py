from enum import Enum
from datetime import datetime
from typing import List

from .SystemSchemas import * #SystemBase, SystemFaction, WaypointType, WaypointTrait, WaypointOrbital, Chart
from .ContractSchemas import TradeSymbol,TransactionBase, SupplyLevel, ActivityLevel
from .AgentSchemas import FactionSymbol

class ShipConditionEventSymbol(Enum):
    REACTOR_OVERLOAD="REACTOR_OVERLOAD"
    ENERGY_SPIKE_FROM_MINERAL="ENERGY_SPIKE_FROM_MINERAL"
    SOLAR_FLARE_INTERFERENCE="SOLAR_FLARE_INTERFERENCE"
    COOLANT_LEAK="COOLANT_LEAK"
    POWER_DISTRIBUTION_FLUCTUATION="POWER_DISTRIBUTION_FLUCTUATION"
    MAGNETIC_FIELD_DISRUPTION="MAGNETIC_FIELD_DISRUPTION"
    HULL_MICROMETEORITE_STRIKES="HULL_MICROMETEORITE_STRIKES"
    STRUCTURAL_STRESS_FRACTURES="STRUCTURAL_STRESS_FRACTURES"
    CORROSIVE_MINERAL_CONTAMINATION="CORROSIVE_MINERAL_CONTAMINATION"
    THERMAL_EXPANSION_MISMATCH="THERMAL_EXPANSION_MISMATCH"
    VIBRATION_DAMAGE_FROM_DRILLING="VIBRATION_DAMAGE_FROM_DRILLING"
    ELECTROMAGNETIC_FIELD_INTERFERENCE="ELECTROMAGNETIC_FIELD_INTERFERENCE"
    IMPACT_WITH_EXTRACTED_DEBRIS="IMPACT_WITH_EXTRACTED_DEBRIS"
    FUEL_EFFICIENCY_DEGRADATION="FUEL_EFFICIENCY_DEGRADATION"
    COOLANT_SYSTEM_AGEING="COOLANT_SYSTEM_AGEING"
    DUST_MICROABRASIONS="DUST_MICROABRASIONS"
    THRUSTER_NOZZLE_WEAR="THRUSTER_NOZZLE_WEAR"
    EXHAUST_PORT_CLOGGING="EXHAUST_PORT_CLOGGING"
    BEARING_LUBRICATION_FADE="BEARING_LUBRICATION_FADE"
    SENSOR_CALIBRATION_DRIFT="SENSOR_CALIBRATION_DRIFT"
    HULL_MICROMETEORITE_DAMAGE="HULL_MICROMETEORITE_DAMAGE"
    SPACE_DEBRIS_COLLISION="SPACE_DEBRIS_COLLISION"
    THERMAL_STRESS="THERMAL_STRESS"
    VIBRATION_OVERLOAD="VIBRATION_OVERLOAD"
    PRESSURE_DIFFERENTIAL_STRESS="PRESSURE_DIFFERENTIAL_STRESS"
    ELECTROMAGNETIC_SURGE_EFFECTS="ELECTROMAGNETIC_SURGE_EFFECTS"
    ATMOSPHERIC_ENTRY_HEAT="ATMOSPHERIC_ENTRY_HEAT"

class ShipComponent(Enum):
    FRAME="FRAME"
    REACTOR="REACTOR"
    ENGINE="ENGINE"

class ShipCrewRotation(Enum):
    Strict="STRICT"
    Relaxed="RELAXED"

class ShipEngineSymbol(Enum):
    ENGINE_IMPULSE_DRIVE_I="ENGINE_IMPULSE_DRIVE_I"
    ENGINE_ION_DRIVE_I="ENGINE_ION_DRIVE_I"
    ENGINE_ION_DRIVE_II="ENGINE_ION_DRIVE_II"
    ENGINE_HYPER_DRIVE_I="ENGINE_HYPER_DRIVE_I"

class ShipModuleSymbol(Enum):
    MODULE_MINERAL_PROCESSOR_I="MODULE_MINERAL_PROCESSOR_I"
    MODULE_GAS_PROCESSOR_I="MODULE_GAS_PROCESSOR_I"
    MODULE_CARGO_HOLD_I="MODULE_CARGO_HOLD_I"
    MODULE_CARGO_HOLD_II="MODULE_CARGO_HOLD_II"
    MODULE_CARGO_HOLD_III="MODULE_CARGO_HOLD_III"
    MODULE_CREW_QUARTERS_I="MODULE_CREW_QUARTERS_I"
    MODULE_ENVOY_QUARTERS_I="MODULE_ENVOY_QUARTERS_I"
    MODULE_PASSENGER_CABIN_I="MODULE_PASSENGER_CABIN_I"
    MODULE_MICRO_REFINERY_I="MODULE_MICRO_REFINERY_I"
    MODULE_ORE_REFINERY_I="MODULE_ORE_REFINERY_I"
    MODULE_FUEL_REFINERY_I="MODULE_FUEL_REFINERY_I"
    MODULE_SCIENCE_LAB_I="MODULE_SCIENCE_LAB_I"
    MODULE_JUMP_DRIVE_I="MODULE_JUMP_DRIVE_I"
    MODULE_JUMP_DRIVE_II="MODULE_JUMP_DRIVE_II"
    MODULE_JUMP_DRIVE_III="MODULE_JUMP_DRIVE_III"
    MODULE_WARP_DRIVE_I="MODULE_WARP_DRIVE_I"
    MODULE_WARP_DRIVE_II="MODULE_WARP_DRIVE_II"
    MODULE_WARP_DRIVE_III="MODULE_WARP_DRIVE_III"
    MODULE_SHIELD_GENERATOR_I="MODULE_SHIELD_GENERATOR_I"
    MODULE_SHIELD_GENERATOR_II="MODULE_SHIELD_GENERATOR_II"

class ShipMountSymbol(Enum):
    MOUNT_GAS_SIPHON_I="MOUNT_GAS_SIPHON_I"
    MOUNT_GAS_SIPHON_II="MOUNT_GAS_SIPHON_II"
    MOUNT_GAS_SIPHON_III="MOUNT_GAS_SIPHON_III"
    MOUNT_SURVEYOR_I="MOUNT_SURVEYOR_I"
    MOUNT_SURVEYOR_II="MOUNT_SURVEYOR_II"
    MOUNT_SURVEYOR_III="MOUNT_SURVEYOR_III"
    MOUNT_SENSOR_ARRAY_I="MOUNT_SENSOR_ARRAY_I"
    MOUNT_SENSOR_ARRAY_II="MOUNT_SENSOR_ARRAY_II"
    MOUNT_SENSOR_ARRAY_III="MOUNT_SENSOR_ARRAY_III"
    MOUNT_MINING_LASER_I="MOUNT_MINING_LASER_I"
    MOUNT_MINING_LASER_II="MOUNT_MINING_LASER_II"
    MOUNT_MINING_LASER_III="MOUNT_MINING_LASER_III"
    MOUNT_LASER_CANNON_I="MOUNT_LASER_CANNON_I"
    MOUNT_MISSILE_LAUNCHER_I="MOUNT_MISSILE_LAUNCHER_I"
    MOUNT_TURRET_I="MOUNT_TURRET_I"

class ShipMountDeposits(Enum):#TODO check if this is just the minerals
    QUARTZ_SAND="QUARTZ_SAND"
    SILICON_CRYSTALS="SILICON_CRYSTALS"
    PRECIOUS_STONES="PRECIOUS_STONES"
    ICE_WATER="ICE_WATER"
    AMMONIA_ICE="AMMONIA_ICE"
    IRON_ORE="IRON_ORE"
    COPPER_ORE="COPPER_ORE"
    SILVER_ORE="SILVER_ORE"
    ALUMINUM_ORE="ALUMINUM_ORE"
    GOLD_ORE="GOLD_ORE"
    PLATINUM_ORE="PLATINUM_ORE"
    DIAMONDS="DIAMONDS"
    URANITE_ORE="URANITE_ORE"
    MERITIUM_ORE="MERITIUM_ORE"

class ShipFlightMode(Enum):
    DRIFT="DRIFT"
    STEALTH="STEALTH"
    CRUISE="CRUISE"
    BURN="BURN"

class ShipNavStatus(Enum):
    IN_TRANSIT="IN_TRANSIT"
    IN_ORBIT="IN_ORBIT"
    DOCKED="DOCKED"

class ShipReactorSymbol(Enum):
    REACTOR_SOLAR_I="REACTOR_SOLAR_I"
    REACTOR_FUSION_I="REACTOR_FUSION_I"
    REACTOR_FISSION_I="REACTOR_FISSION_I"
    REACTOR_CHEMICAL_I="REACTOR_CHEMICAL_I"
    REACTOR_ANTIMATTER_I="REACTOR_ANTIMATTER_I"

class ShipRole(Enum):
    FABRICATOR="FABRICATOR"
    HARVESTER="HARVESTER"
    HAULER="HAULER"
    INTERCEPTOR="INTERCEPTOR"
    EXCAVATOR="EXCAVATOR"
    TRANSPORT="TRANSPORT"
    REPAIR="REPAIR"
    SURVEYOR="SURVEYOR"
    COMMAND="COMMAND"
    CARRIER="CARRIER"
    PATROL="PATROL"
    SATELLITE="SATELLITE"
    EXPLORER="EXPLORER"
    REFINERY="REFINERY"

class ShipType(Enum):
    SHIP_PROBE="SHIP_PROBE"
    SHIP_MINING_DRONE="SHIP_MINING_DRONE"
    SHIP_SIPHON_DRONE="SHIP_SIPHON_DRONE"
    SHIP_INTERCEPTOR="SHIP_INTERCEPTOR"
    SHIP_LIGHT_HAULER="SHIP_LIGHT_HAULER"
    SHIP_COMMAND_FRIGATE="SHIP_COMMAND_FRIGATE"
    SHIP_EXPLORER="SHIP_EXPLORER"
    SHIP_HEAVY_FREIGHTER="SHIP_HEAVY_FREIGHTER"
    SHIP_LIGHT_SHUTTLE="SHIP_LIGHT_SHUTTLE"
    SHIP_ORE_HOUND="SHIP_ORE_HOUND"
    SHIP_REFINING_FREIGHTER="SHIP_REFINING_FREIGHTER"
    SHIP_SURVEYOR="SHIP_SURVEYOR"

class DepositSize(Enum):
    SMALL="SMALL"
    MODERATE="MODERATE"
    LARGE="LARGE"


class Good():
    def __init__(self, JSON):
        self.symbol: TradeSymbol= TradeSymbol(JSON["symbol"])
        self.units: int= JSON["units"]
    def toJSON(self)-> str:
        return{
            "symbol": self.symbol.value,
            "units": self.units
        }

class ShipBase():
    def __init__(self,JSON) -> None:
        self.frame: ShipFrame = ShipFrame(JSON["frame"])
        self.reactor: ShipReactor = ShipReactor(JSON["reactor"])
        self.enginge: ShipEngine = ShipEngine(JSON["engine"])
        self.mounts: List[ShipMount] = [ShipMount(i) for i in JSON["mounts"]]

class ScannedShip(ShipBase):
    def __init__(self, JSON) -> None:
        super().__init__(JSON)
        self.symbol: str = JSON["symbol"]
        self.registration: ShipRegistration=ShipRegistration(JSON["registration"])
        self.nav: ShipNav = ShipNav(JSON["nav"])

class ScannedSystem(SystemBase):
    def __init__(self, JSON) -> None:
        super().__init__(JSON)
        self.distance: int = JSON["distance"]

class ScannedWaypoint():
    def __init__(self,JSON):
        self.symbol: str = JSON["symbol"]
        self.type: WaypointType = WaypointType(JSON["type"])
        self.systemSymbol: str = JSON["systemSymbol"]
        self.x: int = JSON["x"]
        self.y: int = JSON["y"]
        self.orbitals: List[WaypointOrbital] = [WaypointOrbital(i) for i in JSON["orbitals"]]
        self.faction: SystemFaction = SystemFaction(JSON["faction"])
        self.traits: List[WaypointTrait] = [WaypointTrait(i) for i in JSON["traits"]]
        self.chart: Chart = Chart(JSON["chart"])


class Ship(ShipBase):
    def __init__(self,JSON):
        super().__init__(JSON)
        self.symbol: str = JSON["symbol"]
        self.registration: ShipRegistration=ShipRegistration(JSON["registration"])
        self.nav: ShipNav = ShipNav(JSON["nav"])
        self.cooldown: Cooldown = Cooldown(JSON["cooldown"])
        self.cargo: ShipCargo = ShipCargo(JSON["cargo"])
        self.fuel: ShipFuel = ShipFuel(JSON["fuel"])
        self.modules: List[ShipModule] = [ShipModule(i) for i in JSON["modules"]]
        self.crew: ShipCrew = ShipCrew(JSON["crew"])

class ShipCargo():
    def __init__(self, cargoJSON) -> None:
        self.capacity:int=cargoJSON["capacity"]
        self.units:int=cargoJSON["units"]
        self.inventory: List[ShipCargoItem]=[ShipCargoItem(i) for i in cargoJSON["inventory"]]

class ShipCargoItem(): #TODO can inerite from the same as SyphonYield
    def __init__(self,shipCargoItemJSON):
        self.symbol:TradeSymbol = TradeSymbol(shipCargoItemJSON["symbol"])
        self.name:str=shipCargoItemJSON["name"]
        self.description:str=shipCargoItemJSON["description"]
        self.units:int=shipCargoItemJSON["units"]


class ShipConditionEvent():
    def __init__(self,shipConditionEventJSON) -> None:
        self.symbol:ShipConditionEventSymbol=ShipConditionEventSymbol(shipConditionEventJSON["symbol"])
        self.component:ShipComponent=ShipComponent(shipConditionEventJSON["component"])
        self.name:str=shipConditionEventJSON["name"]
        self.description:str=shipConditionEventJSON["description"]

class ShipCrew():
    def __init__(self, JSON):
        self.current:int=JSON["current"]
        self.required:int=JSON["required"]
        self.capacity:int=JSON["capacity"]
        self.rotation:ShipCrewRotation=ShipCrewRotation(JSON["rotation"])
        self.morale:int =JSON["morale"]
        self.wages:int = JSON["wages"]

class ShipComponent():
    '''Base class for all ShipComponents'''
    def __init__(self, JSON):
        self.symbol: str=JSON["symbol"]
        self.name: str= JSON["name"]
        self.description: str = JSON["description"]
        self.requirements: ShipRequirements=ShipRequirements(JSON["requirements"])

class ShipEngine(ShipComponent):
    def __init__(self, JSON):
        super().__init__(JSON)
        self.condition: float= JSON["condition"]
        self.integrity: float= JSON["integrity"]
        self.speed: int= JSON["speed"]

class ShipFrame(ShipComponent):
    def __init__(self, JSON):
        super().__init__(JSON)
        self.condition: float= JSON["condition"]
        self.integrity: float= JSON["integrity"]
        self.moduleSlots: int= JSON["moduleSlots"]
        self.mountingPoints: int= JSON["mountingPoints"]
        self.fuelCapacity: int= JSON["fuelCapacity"]

class ShipFuel():
    def __init__(self, JSON) -> None:
        self.current: int= JSON["current"]
        self.capacity: int = JSON["capacity"]
        self.consumed: ShipFuelConsumed = JSON["consumed"]

class ShipFuelConsumed():
    def __init__(self, JSON) -> None:
        self.amount: int = JSON["amount"]
        self.timestamp: datetime = datetime.fromisoformat(JSON["timestamp"])

class ShipModificationTransaction(TransactionBase):
    def __init__(self, JSON) -> None:
        super().__init__(JSON)
        self.tradeSymbol: TradeSymbol = TradeSymbol(JSON["tradeSymbol"])

class ShipModule(ShipComponent):
    def __init__(self, JSON) -> None:
        super().__init__(JSON)
        self.symbol: ShipModuleSymbol = ShipModuleSymbol(JSON["symbol"])
        self.capacity: int = None
        if "capacity" in JSON:
            self.capacity: int = JSON["capacity"]
        self.range: int = None
        if "range" in JSON:#only some sensors have a range
            self.range: int = JSON["range"]

class ShipMount(ShipComponent):
    def __init__(self, JSON):
        super().__init__(JSON)
        self.symbol: ShipMountSymbol = ShipMountSymbol(JSON["symbol"])
        self.strength: int = JSON["strength"]
        if "deposits" in JSON:#Ship mounts dont have this
            self.deposits: List[ShipMountDeposits] = [ShipMountDeposits(i) for i in JSON["deposits"]]

class ShipNav():
    def __init__(self, JSON):
        self.systemSymbol: str = JSON["systemSymbol"]
        self.waypointSymbol: str = JSON["waypointSymbol"]
        self.route: ShipNavRoute = ShipNavRoute(JSON["route"])
        self.status: ShipNavStatus = ShipNavStatus(JSON["status"])
        self.flightMode: ShipFlightMode = ShipFlightMode(JSON["flightMode"])

class ShipNavRoute():
    def __init__(self,JSON) -> None:
        self.destination: ShipNavRouteWaypoint= ShipNavRouteWaypoint(JSON["destination"])
        self.origin: ShipNavRouteWaypoint= ShipNavRouteWaypoint(JSON["origin"])
        self.departureTime: datetime = datetime.fromisoformat(JSON["departureTime"])
        self.arrival: datetime = datetime.fromisoformat(JSON["arrival"])

class ShipNavRouteWaypoint():
    def __init__(self, JSON) -> None:
        self.symbol: str = JSON["symbol"]
        self.type: WaypointType = WaypointType(JSON["type"])
        self.systemSymbol: str = JSON["systemSymbol"]
        self.x: int = JSON["x"]
        self.y: int = JSON["y"]

class ShipReactor(ShipComponent):
    def __init__(self, JSON):
        super().__init__(JSON)
        self.symbol: ShipReactorSymbol= ShipReactorSymbol(JSON["symbol"])
        self.condition: float= JSON["condition"]
        self.integrity: float= JSON["integrity"]
        self.powerOutput: int= JSON["powerOutput"]
class ShipRegistration():
    def __init__(self, JSON):
        self.name: str= JSON["name"]
        self.factionSymbol: FactionSymbol= FactionSymbol(JSON["factionSymbol"])
        self.role: ShipRole= ShipRole(JSON["role"])

class ShipRequirements():
    def __init__(self, JSON) -> None:
        self.crew: int= JSON["crew"]
        self.slots: int= None
        self.power: int= None
        if "slots" in JSON:
            self.slots: int= JSON["slots"]
                
        if "power" in JSON:
            self.power: int= JSON["power"]
                

class Shipyard():
    def __init__(self, JSON) -> None:
        print(JSON)
        self.symbol: str= JSON["symbol"]
        self.shipTypes: List[ShipType] = [ShipType(i["type"]) for i in JSON["shipTypes"]]
        if "transactions" in JSON: self.transaction: List[ShipyardTransaction] = [ShipyardTransaction(i) for i in JSON["transactions"]]
        else: self.transaction=None
        if "ships" in JSON: self.ships: List[Ship] = [Ship(i) for i in JSON["ships"]]
        else: self.ships = None
        self.modifactionsFee: int = JSON["modificationsFee"]

class ShipyardShip(ShipBase):
    def __init__(self,JSON) -> None:
        super().__init__(JSON)
        self.type: ShipType= ShipType(JSON["type"])
        self.name: str = JSON["name"]
        self.description: str = JSON["description"]
        self.supply: SupplyLevel = SupplyLevel(JSON["description"])
        self.activity: ActivityLevel = ActivityLevel(JSON["activity"])
        self.purchasePrice: int = JSON["purchasePrice"]
        self.modules: List[ShipModule] = [ShipModule(i) for i in JSON["modules"]]
        self.crew: ShipCrew = ShipCrew(JSON["crew"])

class ShipyardTransaction(TransactionBase):
    def __init__(self, JSON) -> None:
        self.shipType: ShipType = ShipType(JSON["shipType"])
        self.price: int = JSON["price"]
        self.agentSymbol: str = JSON["agentSymbol"]


class Syphon():
    def __init__(self, JSON):
        self.shipSymbol: str= JSON["shipSymbol"]
        self.yield_: SyphonYield= SyphonYield(JSON["yield"])

class SyphonYield(Good): #TODO this is the same as extraction yield
    def __init__(self, JSON):
        super.__init__(JSON)

class Survey():
    def __init__(self, JSON):
        self.signature: str= JSON["signature"]
        self.symbol: str= JSON["symbol"]
        self.deposits: List[SurveyDeposit] = [SurveyDeposit(i) for i in JSON["deposits"]]
        self.expiration: datetime = datetime.fromisoformat(JSON["expiration"])
        self.size: DepositSize= DepositSize(JSON["symbol"])

    def toJSON(self):
        return{
        "signature": self.signature,
        "symbol": self.symbol,
        "deposits": [d.symbol.value for d in self.deposits],
        "expiration": self.expiration.isoformat,
        "size": self.size.value
        }

class SurveyDeposit():
    def __init__(self, JSON):
        self.symbol: TradeSymbol = TradeSymbol(JSON["symbol"])

class Extraction():
    def __init__(self,JSON) -> None:
        self.shipSymbol: str = JSON["shipSymbol"]
        self.yield_: ExtractionYield = ExtractionYield(JSON["yield"])

class ExtractionYield(Good): #TODO this is the same as syphon yield
    def __init__(self, JSON):
        super.__init__(JSON)

class Cooldown():
    def __init__(self,JSON) -> None:
        self.shipSymbol: str = JSON["shipSymbol"]
        self.totalSeconds: int = JSON["totalSeconds"]
        self.remainingSeconds: int = JSON["remainingSeconds"]
        self.expiration: datetime=None
        if "expiration" in JSON:
            self.expiration: datetime=datetime.fromisoformat(JSON["expiration"])

