"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/inheritance/materials/greed-specification.html
"""
import time
import random

class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
        _score (int): Keeps player's current score.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 200

    

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._drop_objects(cast)
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _drop_objects(self, cast):
        """Displays Falling Rocks and Gems.

        Args:
            cast (Cast): The cast of actors.
        """
        rocks = cast.get_actors("rocks")
        gems = cast.get_actors("gems")
        
        for rock in rocks:
            rock_y = rock.get_position().get_y()
            time.sleep(0.002)
            rock.get_position().set_y(rock_y + 5)
            if rock_y >= 595:
                rock.get_position().set_y(0)
                rock.get_position().set_x(random.randrange(15, 885, 15))
        

        for gem in gems:
            gem_y = gem.get_position().get_y()
            time.sleep(0.002)
            gem.get_position().set_y(gem_y + 5)
            if gem_y >= 595:
                gem.get_position().set_y(0)
                gem.get_position().set_x(random.randrange(15, 885, 15))
        

        
    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("players")    
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.

        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("players") 
        score = cast.get_first_actor("banners")
        rocks = cast.get_actors("rocks")
        gems = cast.get_actors("gems")

        score.set_text(f"Score: {self._score}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)

      
        # Position Validation
        for gem in gems:
            if gem.get_position().equals(player.get_position()):
                self._score += 5
                score.set_text(f"Score: {self._score}")
        for rock in rocks:    
            if rock.get_position().equals(player.get_position()):
                self._score -= 5
                score.set_text(f"Score: {self._score}")
        


    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
