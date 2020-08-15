class Sailboat(object):
    
    def __init__(self, initial_heading):
        self._heading = initial_heading
        
    def get_heading(self):
        return self._heading  
    
    def change_course(self, course_diff):
        self._heading = (self._heading + course_diff) % 360.0
        
    def set_sail(self, sea):
        self.sea = sea
        
    def get_wind_direction(self):
        try:
        return self.sea.wind_direction
        except:
            raise ValueError("Boat has not been launched.")
