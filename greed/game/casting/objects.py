from game.casting.actor import Actor

class Object(Actor):
    """Falling Object that increases or decreases when in contact with player
        Attributes:
        _score(int): How much to increase/decrease by when in contact with player.
        """

    def __init__(self):
        super().__init__()
        self._score = 0

    def get_score(self):
        """Gets the gem score
        
        Returns:
            int: the score.
        """
        return self._score

    def set_score(self, score):
        """Updates the score to the current score.
        
        Args:
            score (int): The given score.
        """
        self._score = score
