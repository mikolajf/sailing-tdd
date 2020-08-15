def heading_to_rhumb(heading):
    # TODO think of programmatic way
    # with reference to https://en.wikipedia.org/wiki/File:Brosen_windrose_Full.svg

    rhumbs = ['N', 'NbE', 'NNE', 'NEbN', 
              'NE', 'NEbE', 'ENE', 'EbN', 
              'E', 'EbS', 'ESE', 'SEbE', 
              'SE', 'SEbS', 'SSE', 'SbE', 
              'S', 'SbW', 'SSW', 'SWbS', 
              'SW', 'SWbW', 'WSW', 'WbS', 
              'W', 'WbN', 'WNW', 'NWbW', 
              'NW', 'NWbN', 'NNW', 'NbW'
]
    
    points = 32
    angle = 360.0 / points
    index = int((heading + angle / 2 ) // angle)
        
    return rhumbs[index % points]