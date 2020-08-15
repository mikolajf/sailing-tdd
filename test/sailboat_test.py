import unittest
from parameterized import parameterized
from sailboat import Sailboat
from sea import Sea

class SailboatTest(unittest.TestCase):
    
    def test_initial_heading(self):
        sailboat = Sailboat(0.0)
        self.assertEqual(sailboat.get_heading(), 0.0)

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
        
    def test_get_wind_heading_exception(self):
        sea = Sea(0.0)
        sailboat = Sailboat(0.0)
        self.assertRaises(ValueError, sailboat.get_wind_direction)
        
    def test_get_wind_heading_after_launch(self):
        sea = Sea(0.0)
        sailboat = Sailboat(0.0)
        sailboat.set_sail(sea)
        self.assertEqual(sailboat.get_wind_direction(), 0.0)
    
    @parameterized.expand([
        (50.0, 'port'),
        (190.0, 'starboard'),
        (359.0, 'starboard')
    ])   
    def test_get_tack(self, heading, expected_tack):
        sea = Sea(0.0)
        sailboat = Sailboat(heading)
        sailboat.set_sail(sea)
        self.assertEqual(sailboat.get_tack(), expected_tack)

if __name__ == "__main__":
    unittest.main()
