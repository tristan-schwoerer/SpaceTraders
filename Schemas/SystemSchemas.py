from enum import Enum
from datetime import datetime
from typing import List
from .AgentSchemas import Agent, Faction, FactionSymbol
from .ContractSchemas import TradeSymbol

class SystemType(Enum):
    NEUTRON_STAR="NEUTRON_STAR"
    RED_STAR="RED_STAR"
    ORANGE_STAR="ORANGE_STAR"
    BLUE_STAR="BLUE_STAR"
    YOUNG_STAR="YOUNG_STAR"
    WHITE_DWARF="WHITE_DWARF"
    BLACK_HOLE="BLACK_HOLE"
    HYPERGIANT="HYPERGIANT"
    NEBULA="NEBULA"
    UNSTABLE="UNSTABLE"

class WaypointTraitSymbol(Enum):
    UNCHARTED="UNCHARTED"
    UNDER_CONSTRUCTION="UNDER_CONSTRUCTION"
    MARKETPLACE="MARKETPLACE"
    SHIPYARD="SHIPYARD"
    OUTPOST="OUTPOST"
    SCATTERED_SETTLEMENTS="SCATTERED_SETTLEMENTS"
    SPRAWLING_CITIES="SPRAWLING_CITIES"
    MEGA_STRUCTURES="MEGA_STRUCTURES"
    PIRATE_BASE="PIRATE_BASE"
    OVERCROWDED="OVERCROWDED"
    HIGH_TECH="HIGH_TECH"
    CORRUPT="CORRUPT"
    BUREAUCRATIC="BUREAUCRATIC"
    TRADING_HUB="TRADING_HUB"
    INDUSTRIAL="INDUSTRIAL"
    BLACK_MARKET="BLACK_MARKET"
    RESEARCH_FACILITY="RESEARCH_FACILITY"
    MILITARY_BASE="MILITARY_BASE"
    SURVEILLANCE_OUTPOST="SURVEILLANCE_OUTPOST"
    EXPLORATION_OUTPOST="EXPLORATION_OUTPOST"
    MINERAL_DEPOSITS="MINERAL_DEPOSITS"
    COMMON_METAL_DEPOSITS="COMMON_METAL_DEPOSITS"
    PRECIOUS_METAL_DEPOSITS="PRECIOUS_METAL_DEPOSITS"
    RARE_METAL_DEPOSITS="RARE_METAL_DEPOSITS"
    METHANE_POOLS="METHANE_POOLS"
    ICE_CRYSTALS="ICE_CRYSTALS"
    EXPLOSIVE_GASES="EXPLOSIVE_GASES"
    STRONG_MAGNETOSPHERE="STRONG_MAGNETOSPHERE"
    VIBRANT_AURORAS="VIBRANT_AURORAS"
    SALT_FLATS="SALT_FLATS"
    CANYONS="CANYONS"
    PERPETUAL_DAYLIGHT="PERPETUAL_DAYLIGHT"
    PERPETUAL_OVERCAST="PERPETUAL_OVERCAST"
    DRY_SEABEDS="DRY_SEABEDS"
    MAGMA_SEAS="MAGMA_SEAS"
    SUPERVOLCANOES="SUPERVOLCANOES"
    ASH_CLOUDS="ASH_CLOUDS"
    VAST_RUINS="VAST_RUINS"
    MUTATED_FLORA="MUTATED_FLORA"
    TERRAFORMED="TERRAFORMED"
    EXTREME_TEMPERATURES="EXTREME_TEMPERATURES"
    EXTREME_PRESSURE="EXTREME_PRESSURE"
    DIVERSE_LIFE="DIVERSE_LIFE"
    SCARCE_LIFE="SCARCE_LIFE"
    FOSSILS="FOSSILS"
    WEAK_GRAVITY="WEAK_GRAVITY"
    STRONG_GRAVITY="STRONG_GRAVITY"
    CRUSHING_GRAVITY="CRUSHING_GRAVITY"
    TOXIC_ATMOSPHERE="TOXIC_ATMOSPHERE"
    CORROSIVE_ATMOSPHERE="CORROSIVE_ATMOSPHERE"
    BREATHABLE_ATMOSPHERE="BREATHABLE_ATMOSPHERE"
    THIN_ATMOSPHERE="THIN_ATMOSPHERE"
    JOVIAN="JOVIAN"
    ROCKY="ROCKY"
    VOLCANIC="VOLCANIC"
    FROZEN="FROZEN"
    SWAMP="SWAMP"
    BARREN="BARREN"
    TEMPERATE="TEMPERATE"
    JUNGLE="JUNGLE"
    OCEAN="OCEAN"
    RADIOACTIVE="RADIOACTIVE"
    MICRO_GRAVITY_ANOMALIES="MICRO_GRAVITY_ANOMALIES"
    DEBRIS_CLUSTER="DEBRIS_CLUSTER"
    DEEP_CRATERS="DEEP_CRATERS"
    SHALLOW_CRATERS="SHALLOW_CRATERS"
    UNSTABLE_COMPOSITION="UNSTABLE_COMPOSITION"
    HOLLOWED_INTERIOR="HOLLOWED_INTERIOR"
    STRIPPED="STRIPPED"

class WaypointType(Enum):
    PLANET="PLANET"
    GAS_GIANT="GAS_GIANT"
    MOON="MOON"
    ORBITAL_STATION="ORBITAL_STATION"
    JUMP_GATE="JUMP_GATE"
    ASTEROID_FIELD="ASTEROID_FIELD"
    ASTEROID="ASTEROID"
    ENGINEERED_ASTEROID="ENGINEERED_ASTEROID"
    ASTEROID_BASE="ASTEROID_BASE"
    NEBULA="NEBULA"
    DEBRIS_FIELD="DEBRIS_FIELD"
    GRAVITY_WELL="GRAVITY_WELL"
    ARTIFICIAL_GRAVITY_WELL="ARTIFICIAL_GRAVITY_WELL"
    FUEL_STATION="FUEL_STATION"

class WaypointModifierSymbol(Enum):
    STRIPPED="STRIPPED"
    UNSTABLE="UNSTABLE"
    RADIATION_LEAK="RADIATION_LEAK"
    CRITICAL_LIMIT="CRITICAL_LIMIT"
    CIVIL_UNREST="CIVIL_UNREST"

class SystemBase():
    def __init__(self, JSON):
        self.symbol: str= JSON["symbol"]
        self.sectorSymbol: str= JSON["sectorSymbol"]
        self.type: SystemType= SystemType(JSON["type"])
        self.x: int = JSON["x"]
        self.y: int = JSON["y"]

class ConnectedSystem(SystemBase):
    def __init__(self, JSON) -> None:
        super().__init__(JSON)
        self.factionSymbol: FactionSymbol= FactionSymbol(JSON["factionSymbol"])
        self.distance: int = JSON["distance"]

class System(SystemBase):
    def __init__(self, JSON):
        super().__init__(JSON)
        self.waypoints=[Waypoint(i) for i in JSON["waypoints"]]
        self.factions=[Faction(i) for i in JSON["factions"]]

class SystemFaction():#TODO could be the Base Class for Faction class
    def __init__(self, JSON) -> None:
        self.symbol:FactionSymbol=FactionSymbol(JSON["symbol"])

class SystemWaypoint():
    def __init__(self, JSON) -> None:
        self.symbol: str = JSON["symbol"]
        self.type: WaypointType = WaypointType(JSON["type"])
        self.x: int = JSON["x"]
        self.y: int = JSON["y"]
        self.orbitals: List[str] = JSON["orbitals"]
        self.orbits: str = JSON["orbits"]


class Waypoint():
    def __init__(self,JSON):
        self.symbol: str = JSON["symbol"]
        self.type: WaypointType = WaypointType(JSON["type"])
        self.x: int = JSON["x"]
        self.y: int = JSON["y"]
        self.orbitals: List[WaypointOrbital] = [WaypointOrbital(i) for i in JSON["orbitals"]]
        self.orbits: str = JSON["orbits"]
        self.factions: SystemFaction = SystemFaction(JSON["faction"])
        self.traits: List[WaypointTrait] = [WaypointTrait(i) for i in JSON["traits"]]
        self.modifiers: List[WaypointModifier] = [WaypointModifier(i) for i in JSON["modifiers"]]
        self.chart: Chart = Chart(JSON["chart"])
        self.isUnderConstruction: bool = JSON["isUnderConstruction"]

class WaypointFaction():
    def __init__(self, JSON):
        self.symbol:FactionSymbol=FactionSymbol(JSON["symbol"])

class WaypointModifier():
    def __init__(self, JSON):
        self.symbol: WaypointModifierSymbol=WaypointModifierSymbol(JSON["symbol"])
        self.name: str= JSON["name"]
        self.description: str= JSON["description"]

class WaypointOrbital():
    def __init__(self, JSON):
        self.symbol: str = JSON["symbol"]

class WaypointTrait():
    def __init__(self, JSON) -> None:
        self.symbol: WaypointTraitSymbol= WaypointTraitSymbol(JSON["symbol"])
        self.name: str= JSON["name"]
        self.description: str= JSON["description"]


class Chart():
    def __init__(self,JSON):
        self.waypointSymbol: str=JSON["waypointSymbol"]
        self.submittedBy: Agent=Agent(JSON["submittedBy"]) #TODO this might be just the agentsymbol
        self.submittedOn: datetime=datetime.fromisoformat(JSON["submittedOn"])

class JumpGate():
    def __init__(self, JSON) -> None:
        self.symbol: str = JSON["symbol"]
        self.connections: List[str] = [i for i in JSON["connections"]]

class Construction():
    def __init__(self, JSON) -> None:
        self.symbol: str = JSON["symbol"]
        self.materials: List[ConstructionMaterial] = JSON["symbol"]
        self.isVomplete: bool = JSON["isComplete"]

class ConstructionMaterial():
    def __init__(self,JSON) -> None:
        self.tradeSymbol:TradeSymbol = TradeSymbol(JSON["tradeSymbol"])
        self.required: int = JSON["required"]
        self.fulfilled: int = JSON["fulfilled"]


