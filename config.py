import types
class config():
    # Unused modular config
    def __init__(self):
        self.keys = types.SimpleNamespace()
        keys = self.keys
        self.keys.movement = types.SimpleNamespace()
        keys.movement.wasd = types.SimpleNamespace()
        
        wasd = keys.movement.wasd
        wasd.north = 'w'
        wasd.south = 's'
        wasd.west = 'a'
        wasd.east = 'd'
        wasd.northwest = 'q'
        wasd.northeast = 'e'
        wasd.southwest = 'z'
        wasd.southeast = 'c'
        keys.movement.numpad = types.SimpleNamespace()
        numpad = keys.movement.numpad
        numpad.north = '8'
        numpad.south = '2'
        numpad.west = '4'
        numpad.east = '6'
        numpad.northwest = '7'
        numpad.northeast = '9'
        numpad.southwest = '1'
        numpad.southeast = '3'
        keys.movement.arrows = types.SimpleNamespace()
        arrows = keys.movement.arrows
        arrows.north = 'up'
        arrows.south = 'down'
        arrows.west = 'left'
        arrows.east = 'right'
        arrows.northwest = 'home'
        arrows.northeast = 'pageup'
        arrows.southwest = 'end'
        arrows.southeast = 'pagedown'