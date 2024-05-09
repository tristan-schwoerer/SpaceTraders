from enum import Enum
from datetime import datetime
from typing import List

class FactionSymbol(Enum):
    COSMIC="COSMIC"
    VOID="VOID"
    GALACTIC="GALACTIC"
    QUANTUM="QUANTUM"
    DOMINION="DOMINION"
    ASTRO="ASTRO"
    CORSAIRS="CORSAIRS"
    OBSIDIAN="OBSIDIAN"
    AEGIS="AEGIS"
    UNITED="UNITED"
    SOLITARY="SOLITARY"
    COBALT="COBALT"
    OMEGA="OMEGA"
    ECHO="ECHO"
    LORDS="LORDS"
    CULT="CULT"
    ANCIENTS="ANCIENTS"
    SHADOW="SHADOW"
    ETHEREAL="ETHEREAL"

class FactionTraitSymbol(Enum):
    BUREAUCRATIC="BUREAUCRATIC"
    SECRETIVE="SECRETIVE"
    CAPITALISTIC="CAPITALISTIC"
    INDUSTRIOUS="INDUSTRIOUS"
    PEACEFUL="PEACEFUL"
    DISTRUSTFUL="DISTRUSTFUL"
    WELCOMING="WELCOMING"
    SMUGGLERS="SMUGGLERS"
    SCAVENGERS="SCAVENGERS"
    REBELLIOUS="REBELLIOUS"
    EXILES="EXILES"
    PIRATES="PIRATES"
    RAIDERS="RAIDERS"
    CLAN="CLAN"
    GUILD="GUILD"
    DOMINION="DOMINION"
    FRINGE="FRINGE"
    FORSAKEN="FORSAKEN"
    ISOLATED="ISOLATED"
    LOCALIZED="LOCALIZED"
    ESTABLISHED="ESTABLISHED"
    NOTABLE="NOTABLE"
    DOMINANT="DOMINANT"
    INESCAPABLE="INESCAPABLE"
    INNOVATIVE="INNOVATIVE"
    BOLD="BOLD"
    VISIONARY="VISIONARY"
    CURIOUS="CURIOUS"
    DARING="DARING"
    EXPLORATORY="EXPLORATORY"
    RESOURCEFUL="RESOURCEFUL"
    FLEXIBLE="FLEXIBLE"
    COOPERATIVE="COOPERATIVE"
    UNITED="UNITED"
    STRATEGIC="STRATEGIC"
    INTELLIGENT="INTELLIGENT"
    RESEARCH_FOCUSED="RESEARCH_FOCUSED"
    COLLABORATIVE="COLLABORATIVE"
    PROGRESSIVE="PROGRESSIVE"
    MILITARISTIC="MILITARISTIC"
    TECHNOLOGICALLY_ADVANCED="TECHNOLOGICALLY_ADVANCED"
    AGGRESSIVE="AGGRESSIVE"
    IMPERIALISTIC="IMPERIALISTIC"
    TREASURE_HUNTERS="TREASURE_HUNTERS"
    DEXTEROUS="DEXTEROUS"
    UNPREDICTABLE="UNPREDICTABLE"
    BRUTAL="BRUTAL"
    FLEETING="FLEETING"
    ADAPTABLE="ADAPTABLE"
    SELF_SUFFICIENT="SELF_SUFFICIENT"
    DEFENSIVE="DEFENSIVE"
    PROUD="PROUD"
    DIVERSE="DIVERSE"
    INDEPENDENT="INDEPENDENT"
    SELF_INTERESTED="SELF_INTERESTED"
    FRAGMENTED="FRAGMENTED"
    COMMERCIAL="COMMERCIAL"
    FREE_MARKETS="FREE_MARKETS"
    ENTREPRENEURIAL="ENTREPRENEURIAL"


class Agent():
    def __init__(self,JSON):
        # default attributes
        self.symbol:str=JSON["symbol"]
        self.headquarters:str=JSON["headquarters"]
        self.credits:int=JSON["credits"]
        self.startingFaction:FactionSymbol=FactionSymbol(JSON["startingFaction"])
        self.shipCount:int=JSON["shipCount"]
        try:
            self.accountID:str=JSON["accountID"]#this is only returned for our own agent
        except:
            self.accountID:str=None#this is only returned for our own agent



class Faction():
    def __init__(self, JSON):
        self.symbol:FactionSymbol=FactionSymbol(JSON["symbol"])
        self.name: str = JSON["name"]
        self.description: str = JSON["description"]
        self.headquarters: str = JSON["headquarters"]
        self.traits: List[FactionTrait] = [FactionTrait(i) for i in JSON["traits"]]
        self.isRecruiting: bool = JSON["isRecruiting"]

class FactionTrait():
    def __init__(self, JSON) -> None:
        self.symbol: FactionTraitSymbol = FactionTraitSymbol(JSON["symbol"])
        self.name: str = JSON["name"]
        self.description: str = JSON["description"]