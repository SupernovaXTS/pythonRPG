import types
class config():
    # Unused modular config
    def __init__(self):
        self.keys = types.SimpleNamespace()
        self.keys.movement = types.SimpleNamespace()
        self.keys.movement.wasd = types.SimpleNamespace()
        wasd = self.keys.movement.wasd
        wasd.forward = 'w'
        wasd.back = 's'
        wasd.left = 'a'
        wasd.right = 'd'
        self.keys.movement.numpad = types.SimpleNamespace()
        numpad = self.keys.movement.numpad
        
