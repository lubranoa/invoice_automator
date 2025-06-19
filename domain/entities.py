from dataclasses import dataclass
from value_objects import Department

@dataclass
class JobInfo:
    """"""
    job_number: str
    department: Department
    ins_carrier: str
    ins_adjuster: str
    client_name: str
    address_line_1: str
    address_line_2: str
    claim_no: str
    
@dataclass
class InvoiceInfo:
    """"""
    invoice_no: str
    #TODO: add more
    