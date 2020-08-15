import unittest
from sailboat import Sailboat

class SailboatTest(unittest.TestCase):
    
    def test_initial_heading(self):
        sailboat = Sailboat(0.0)
        self.assertEqual(sailboat.get_heading(), 0.0)


if __name__ == "__main__":
    unittest.main()
