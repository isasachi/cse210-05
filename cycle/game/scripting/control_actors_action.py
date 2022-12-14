import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction_1 = Point(constants.CELL_SIZE, 0)
        self._direction_2 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        cycle_1 = cast.get_actors("cycles")[0]
        cycle_2 = cast.get_actors("cycles")[1]

        if cycle_1.get_color() == constants.RED:
            # left
            if self._keyboard_service.is_key_down('a'):
                self._direction_1 = Point(-constants.CELL_SIZE, 0)
            
            # right
            if self._keyboard_service.is_key_down('d'):
                self._direction_1 = Point(constants.CELL_SIZE, 0)
            
            # up
            if self._keyboard_service.is_key_down('w'):
                self._direction_1 = Point(0, -constants.CELL_SIZE)
            
            # down
            if self._keyboard_service.is_key_down('s'):
                self._direction_1 = Point(0, constants.CELL_SIZE)

        if cycle_2.get_color() == constants.GREEN:
            # left
            if self._keyboard_service.is_key_down('j'):
                self._direction_2 = Point(-constants.CELL_SIZE, 0)
            
            # right
            if self._keyboard_service.is_key_down('l'):
                self._direction_2 = Point(constants.CELL_SIZE, 0)
            
            # up
            if self._keyboard_service.is_key_down('i'):
                self._direction_2 = Point(0, -constants.CELL_SIZE)
            
            # down
            if self._keyboard_service.is_key_down('k'):
                self._direction_2 = Point(0, constants.CELL_SIZE)
        
        cycle_1.turn_head(self._direction_1)
        cycle_2.turn_head(self._direction_2)