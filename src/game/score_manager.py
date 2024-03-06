# score_manager.py

class ScoreManager:
    def __init__(self):
        """
        Initialize the Score Manager.
        """
        self.score = 0
        self.high_scores = []  # List to store high scores

    def add_score(self, points):
        """
        Add points to the current score.

        :param points: Number of points to add to the score.
        """
        self.score += points

    def reset_score(self):
        """
        Reset the current score to zero.
        """
        self.score = 0

    def update_high_scores(self):
        """
        Update the high scores list with the current score.
        """
        self.high_scores.append(self.score)
        self.high_scores.sort(reverse=True)  # Sort scores in descending order
        self.high_scores = self.high_scores[:5]  # Keep only top 5 scores

    def get_high_scores(self):
        """
        Get the list of high scores.

        :return: List of high scores.
        """
        return self.high_scores

    def get_current_score(self):
        """
        Get the current score.

        :return: The current score.
        """
        return self.score

# Example usage (commented out)
# score_manager = ScoreManager()
# score_manager.add_score(100)
# score_manager.update_high_scores()
# print(score_manager.get_high_scores())
# score_manager.reset_score()
