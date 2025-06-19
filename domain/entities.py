from dataclasses import dataclass
from value_objects import Department
from typing import List, Optional

@dataclass
class JobInfo:
    """"""
    job_number: str
    location: str
    department: Department
    ins_carrier: str
    ins_adjuster: str = ""
    client_name: str
    address_line_1: str
    address_line_2: str = ""
    address_line_3: str
    claim_no: str
    
@dataclass
class Invoice:
    """"""
    invoice_no: str
    #TODO: add more
    