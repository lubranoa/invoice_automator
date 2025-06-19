import unittest

from context import domain
from domain.value_objects import Department as dept
from domain.value_objects import InvoiceType as invo


class TestDomainModels(unittest.TestCase):
    
    def test_department_models(self):
        """Tests that Department class contains the correct values and names.
        """
        self.assertEqual(dept.CON.value, 'CON')
        self.assertEqual(dept.CON.name, 'CON')
        self.assertEqual(dept.ELE.value, 'ELE')
        self.assertEqual(dept.ELE.name, 'ELE')
        self.assertEqual(dept.FBR.value, 'FBR')
        self.assertEqual(dept.FBR.name, 'FBR')
        
    def test_invoice_type_models(self):
        """Tests that InvoiceType class contains correct values.
        """
        self.assertEqual(invo.CLN.value, 'clean')
        self.assertEqual(invo.EST.value, 'estimate')
        self.assertEqual(invo.INS.value, 'inspect')
        self.assertEqual(invo.PCK.value, 'pack')
        self.assertEqual(invo.STR.value, 'storage')
        self.assertEqual(invo.TLI.value, 'tli')
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
