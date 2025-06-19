from enum import Enum, StrEnum

class Department(StrEnum):
    """Department codes.
    """
    CON = "CON"
    ELE = "ELE"
    FBR = "FBR"
    
class InvoiceType(StrEnum):
    """Types of invoice workflows supported.
    """
    CLN = "clean"
    EST = "estimate"
    INS = "inspect"
    PCK = "pack"
    STR = "storage"
    TLI = "tli"
        