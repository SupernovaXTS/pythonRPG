import types
class config():
    # Unused modular config
    def __init__(self):
        self.keys = types.SimpleNamespace()
        self.keys.movement = types.SimpleNamespace()
        self.keys.movement.wasd = types.SimpleNamespace()
        wasd = self.keys.movement.wasd
        wasd.north = 'w'
        wasd.south = 's'
        wasd.west = 'a'
        wasd.east = 'd'
        wasd.northwest = 'q'
        wasd.northeast = 'e'
        wasd.southwest = 'z'
        wasd.southeast = 'c'
        self.keys.movement.numpad = types.SimpleNamespace()
        numpad = self.keys.movement.numpad
        numpad.north = '8'
        numpad.south = '2'
        numpad.west = '4'
        numpad.east = '6'
        numpad.northwest = '7'
        numpad.northeast = '9'
        numpad.southwest = '1'
        numpad.southeast = '3'
