import unittest

from context import domain
from domain.value_objects import Department as dept


class TestDomainModels(unittest.TestCase):
    
    def test_department_models(self):
        """_summary_
        """
        self.assertEqual(dept.CON.value, 'CON')
        self.assertEqual(dept.ELE.value, 'ELE')
        self.assertEqual(dept.FBR.value, 'FBR')
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
