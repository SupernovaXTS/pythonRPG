from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import tcod

from actions import (
    Action,
    BumpAction,
    EscapeAction,
    WaitAction
)
import color
import exceptions

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
CURSOR_Y_KEYS = {
    events.UP: -1,
    events.DOWN: 1,
    events.PAGEUP: -10,
    events.PAGEDOWN: 10,
}

WAIT_KEYS = {
    events.PERIOD,
    events.KP_5,
    events.CLEAR,
}

class EventHandler(tcod.event.EventDispatch[Action]):
    def __init__(self, engine: Engine):
        self.engine = engine
    def handle_events(self, event: tcod.event.Event) -> None:
        self.handle_action(self.dispatch(event))

    def handle_action(self, action: Optional[Action]) -> bool:
        """Handle actions returned from event methods.

        Returns True if the action will advance a turn.
        """
        if action is None:
            return False

        try:
            action.perform()
        except exceptions.Impossible as exc:
            self.engine.message_log.add_message(exc.args[0], color.impossible)
            return False  # Skip enemy turn on exceptions.

        self.engine.handle_enemy_turns()

        self.engine.update_fov()
        return True
    def on_render(self, console: tcod.Console) -> None:
       self.engine.render(console)
    def ev_mousemotion(self, event: tcod.event.MouseMotion) -> None:        
        if self.engine.game_map.in_bounds(event.tile.x, event.tile.y):
            self.engine.mouse_location = event.tile.x, event.tile.y

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
class MainGameEventHandler(EventHandler):

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
        elif key == events.V:
            self.engine.event_handler = HistoryViewer(self.engine)
    
        # No valid key was pressed
        return action
class GameOverEventHandler(EventHandler):
    def ev_keydown(self, event: tcod.event.KeyDown) -> None:
        key = event.sym
        if key == events.ESCAPE:
            raise SystemExit()
class HistoryViewer(EventHandler):
    """Print the history on a larger window which can be navigated."""

    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.log_length = len(engine.message_log.messages)
        self.cursor = self.log_length - 1

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)  # Draw the main state as the background.

        log_console = tcod.Console(console.width - 6, console.height - 6)

        # Draw a frame with a custom banner title.
        log_console.draw_frame(0, 0, log_console.width, log_console.height)
        log_console.print_box(
            0, 0, log_console.width, 1, "┤Message history├", alignment=tcod.CENTER
        )

        # Render the message log using the cursor parameter.
        self.engine.message_log.render_messages(
            log_console,
            1,
            1,
            log_console.width - 2,
            log_console.height - 2,
            self.engine.message_log.messages[: self.cursor + 1],
        )
        log_console.blit(console, 3, 3)

    def ev_keydown(self, event: tcod.event.KeyDown) -> None:
        # Fancy conditional movement to make it feel right.
        if event.sym in CURSOR_Y_KEYS:
            adjust = CURSOR_Y_KEYS[event.sym]
            if adjust < 0 and self.cursor == 0:
                # Only move from the top to the bottom when you're on the edge.
                self.cursor = self.log_length - 1
            elif adjust > 0 and self.cursor == self.log_length - 1:
                # Same with bottom to top movement.
                self.cursor = 0
            else:
                # Otherwise move while staying clamped to the bounds of the history log.
                self.cursor = max(0, min(self.cursor + adjust, self.log_length - 1))
        elif event.sym == events.HOME:
            self.cursor = 0  # Move directly to the top message.
        elif event.sym == events.END:
            self.cursor = self.log_length - 1  # Move directly to the last message.
        else:  # Any other key moves back to the main game state.
            self.engine.event_handler = MainGameEventHandler(self.engine)