import types
class config():
    # Unused modular config
    def __init__(self):
        self.layouts = types.SimpleNamespace()
        layouts = self.layouts
        
        layouts.default = 'wasd'
        layouts.available = ['wasd', 'numpad', 'arrows']
        layouts.current = layouts.default
        # Special actions not tied to movement
        layouts.special = types.SimpleNamespace()
        special = layouts.special
        special.escape = 'ESCAPE'
        special.inventory = 'I'
        special.drop = 'H'
        special.pickup = 'G'
        special.character_screen = 'B'
        special.look = 'SLASH'

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
        wasd.north = 'W'
        wasd.south = 'S'
        wasd.west = 'A'
        wasd.east = 'D'
        wasd.northwest = 'Q'
        wasd.northeast = 'E'
        wasd.southwest = 'Z'
        wasd.southeast = 'C'
        wasd.wait = 'X'
        wasd.confirm = 'RETURN'
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
        numpad.confirm = 'KP_ENTER'
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
        arrows.confirm = 'RETURN'

        layouts.cursor = types.SimpleNamespace()
        cursor = layouts.cursor
        cursor.up = 'UP'
        cursor.down = 'DOWN'
        cursor.up10 = 'PAGEUP'
        cursor.down10 = 'PAGEDOWN'
    def get_layout(self):
        return getattr(self.layouts, self.layouts.current)
    def set_layout(self, layout_name):
        if layout_name in self.layouts.available:
            self.layouts.current = layout_name
        else:
            raise ValueError(f"Layout '{layout_name}' is not available.")
    def movementHandler(layout,key):
        if key in layout:
            dx, dy = getattr(super.layouts.directions, key)
            return [dx, dy]
        return None