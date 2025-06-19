from enum import Enum

class Department(Enum):
    """Department codes."""
    CON = "CON"
    ELE = "ELE"
    FBR = "FBR"
    

class InvoiceType(Enum):
    """Types of invoice workflows supported."""
    CLN = "clean"
    EST = "estimate"
    INS = "inspect"
    PCK = "pack"
    STR = "storage"
    TLI = "tli"
