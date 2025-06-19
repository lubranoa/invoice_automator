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

class Pricing(Enum):
    """Pre-set pricing for sales tax and total loss inventory fees.
    """
    S_TAX = 0.0825
    TLI_BASE = 950
    TLI_ADDTL = 1.5
    TLI_DRIVE = 50
    TLI_VALU = 1.75
        