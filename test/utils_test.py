import unittest
from utils import heading_to_rhumb
from parameterized import parameterized

class UtilsTest(unittest.TestCase):
    @parameterized.expand([
        (0.0, 'N'),
        (350.0, 'NbW'),
        (15.0, 'NbE'),
        (180.0, 'S'),
        (124.0, 'SEbE')
    ])      
    def test_heading_to_rhumb(self, heading, expected_rhumb):
        self.assertEqual(heading_to_rhumb(heading), expected_rhumb)