import types
class config():
    # Unused modular config
    def __init__(self):
        self.layouts = types.SimpleNamespace()
        layouts = self.layouts
        
        # Directions for mapping to existing input handlers
        layouts.directions = types.SimpleNamespace()
        directions = layouts.directions
        directions.north = (0, -1)
        directions.south = (0, 1)
        directions.west = (-1, 0)
        directions.east = (1, 0)
        directions.northwest = (-1, -1)
        directions.northeast = (1, -1)
        directions.southwest = (-1, 1)
        directions.southeast = (1, 1)
        layouts.wasd = types.SimpleNamespace()
        
        wasd = layouts.wasd
        wasd.north = 'w'
        wasd.south = 's'
        wasd.west = 'a'
        wasd.east = 'd'
        wasd.northwest = 'q'
        wasd.northeast = 'e'
        wasd.southwest = 'z'
        wasd.southeast = 'c'
        wasd.wait = 'x'
        layouts.numpad = types.SimpleNamespace()
        numpad = layouts.numpad
        numpad.north = 'KP_8'
        numpad.south = 'KP_2'
        numpad.west = 'KP_4'
        numpad.east = 'KP_6'
        numpad.northwest = 'KP_7'
        numpad.northeast = 'KP_9'
        numpad.southwest = 'KP_1'
        numpad.southeast = 'KP_3'
        numpad.wait = 'KP_5'
        layouts.arrows = types.SimpleNamespace()
        arrows = layouts.arrows
        arrows.north = 'up'
        arrows.south = 'down'
        arrows.west = 'left'
        arrows.east = 'right'
        arrows.northwest = 'home'
        arrows.northeast = 'pageup'
        arrows.southwest = 'end'
        arrows.southeast = 'pagedown'
        arrows.wait = 'clear'
        layouts.cursor = types.SimpleNamespace()
        cursor = layouts.cursor
        cursor.up = 'UP'
        cursor.down = 'DOWN'
        cursor.up10 = 'PAGEUP'
        cursor.down10 = 'PAGEDOWN'