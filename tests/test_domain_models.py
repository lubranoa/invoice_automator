import unittest, os
from src.core.domain.types import Department

class TestDomainModels(unittest.TestCase):
    
    def test_department_models(self):
        self.assertEqual(Department.CON.value, 'CON')
        self.assertEqual(Department.ELE.value, 'ELE')
        self.assertEqual(Department.FBR.value, 'FBR')
        
if __name__ == '__main__':
    unittest.main()
