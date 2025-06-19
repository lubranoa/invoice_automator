from enum import Enum, StrEnum

class Locations(StrEnum):
    """Locations and codes.
    """
    AUS = "144"
    DFW = "153"
    HOU = "145"
    CORP = "20"

class Department(StrEnum):
    """Department codes.
    """
    CON = "CON"
    ELE = "ELE"
    FBR = "FBR"
    INV = "INV"
    
class InvoiceType(StrEnum):
    """Types of invoice workflows supported.
    """
    CLN = "clean"
    EST = "estimate"
    INS = "inspect"
    PCK = "pack"
    STR = "storage"
    TLI = "tli"
        