import unittest
from parameterized import parameterized
from sailboat import Sailboat

class SailboatTest(unittest.TestCase):
    
    def test_initial_heading(self):
        sailboat = Sailboat(0.0)
        self.assertEqual(sailboat.get_heading(), 0.0)
    
    @parameterized.expand([
        (0.0, 'N'),
        (350.0, 'N'),
        (10.0, 'N')
    ])      
    def test_initial_rhumb(self, initial_heading, expected_rhumb):
        sailboat = Sailboat(initial_heading)
        self.assertEqual(sailboat.get_rhumb(), expected_rhumb)

    @parameterized.expand([
        (0.0, 10.0, 10.0),
        (0.0, 90.0, 90.0),
        (270.0, 100.0, 10.0)
    ])        
    def test_change_course_to_starboard(self, initial_heading, course_diff, end_heading):
        sailboat = Sailboat(initial_heading)
        sailboat.change_course(course_diff)
        self.assertEqual(sailboat.get_heading(), end_heading)
        
    @parameterized.expand([
        (0.0, -10.0, 350.0),
        (0.0, -90.0, 270.0),
        (270.0, -100.0, 170.0)
    ])        
    def test_change_course_to_portside(self, initial_heading, course_diff, end_heading):
        sailboat = Sailboat(initial_heading)
        sailboat.change_course(course_diff)
        self.assertEqual(sailboat.get_heading(), end_heading)

if __name__ == "__main__":
    unittest.main()
