# score_manager.py
import pygame

class ScoreManager:
    def __init__(self, font, screen):
        """
        Initialize the Score Manager with PyGame.

        :param font: PyGame font for rendering text.
        :param screen: PyGame screen to display the scores.
        """
        self.score = 0
        self.high_scores = []  # List to store high scores
        self.font = font
        self.screen = screen

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

    def display_scores(self):
        """
        Display the current score and high scores on the screen.
        """
        # Display Current Score
        current_score_text = f"Score: {self.score}"
        current_score_surface = self.font.render(current_score_text, True, (255, 255, 255))
        self.screen.blit(current_score_surface, (20, 100))

        # Display High Scores
        for i, high_score in enumerate(self.high_scores):
            high_score_text = f"High Score {i+1}: {high_score}"
            high_score_surface = self.font.render(high_score_text, True, (255, 255, 255))
            self.screen.blit(high_score_surface, (20, 130 + i*30))

# Example usage (commented out)
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# font = pygame.font.Font(None, 36)
# score_manager = ScoreManager(font, screen)
# score_manager.add_score(100)
# score_manager.update_high_scores()
# score_manager.display_scores()
# pygame.quit()
