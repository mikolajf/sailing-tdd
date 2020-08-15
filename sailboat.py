class Sailboat(object):
    
    def __init__(self, initial_heading):
        self._heading = initial_heading
        
    def get_heading(self):
        return self._heading  
    
    def change_course(self, course_diff):
        self._heading = (self._heading + course_diff) % 360.0
        
    def get_rhumb(self):
        compass = ['N', 'E', 'S', 'W']
        index_main = int((self._heading + 45.0) // 90.0)
        return compass[index_main % 4]