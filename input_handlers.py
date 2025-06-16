from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import tcod.event

from actions import Action, BumpAction, EscapeAction, WaitAction

if TYPE_CHECKING:
    from engine import Engine
events = tcod.event.KeySym
MOVE_KEYS = {
    # Arrow keys.
    events.UP: (0, -1),
    events.DOWN: (0, 1),
    events.LEFT: (-1, 0),
    events.RIGHT: (1, 0),
    events.HOME: (-1, -1),
    events.END: (-1, 1),
    events.PAGEUP: (1, -1),
    events.PAGEDOWN: (1, 1),
    # Numpad keys.
    events.KP_1: (-1, 1),
    events.KP_2: (0, 1),
    events.KP_3: (1, 1),
    events.KP_4: (-1, 0),
    events.KP_6: (1, 0),
    events.KP_7: (-1, -1),
    events.KP_8: (0, -1),
    events.KP_9: (1, -1),
    # Vi keys.
    events.H: (-1, 0),
    events.J: (0, 1),
    events.K: (0, -1),
    events.L: (1, 0),
    events.Y: (-1, -1),
    events.U: (1, -1),
    events.B: (-1, 1),
    events.N: (1, 1),
}

WAIT_KEYS = {
    events.PERIOD,
    events.KP_5,
    events.CLEAR,
}

class EventHandler(tcod.event.EventDispatch[Action]):
    def __init__(self, engine: Engine):
        self.engine = engine
    def handle_events(self) -> None:
        raise NotImplementedError()

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
class MainGameEventHandler(EventHandler):

    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()

            self.engine.handle_enemy_turns()
            self.engine.update_fov()  # Update the FOV before the players next action.

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym
        player = self.engine.player

        if key in MOVE_KEYS:
            dx, dy = MOVE_KEYS[key]
            action = BumpAction(player, dx, dy) # type: ignore
        elif key in WAIT_KEYS:
            action = WaitAction(player) # type: ignore

        elif key == events.ESCAPE:
            action = EscapeAction(player) # type: ignore

        # No valid key was pressed
        return action
class GameOverEventHandler(EventHandler):
    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == events.ESCAPE:
            action = EscapeAction(self.engine.player)

        # No valid key was pressed
        return action
