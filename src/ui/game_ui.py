# game_ui.py
import pygame

class GameUI:
    def __init__(self, screen, font):
        """
        Initialize the game's user interface with PyGame.

        :param screen: PyGame screen to display the UI.
        :param font: PyGame font for text rendering.
        """
        self.screen = screen
        self.font = font
        self.health = 10
        self.max_health = 10
        self.score = 0
        self.inventory = []

    def update_health(self, health):
        """
        Update the health value.

        :param health: Integer representing the player's current health.
        """
        self.health = health

    def update_score(self, score):
        """
        Update the score value.

        :param score: Integer representing the player's current score.
        """
        self.score = score

    def update_inventory(self, inventory):
        """
        Update the inventory list.

        :param inventory: List representing the player's current inventory.
        """
        self.inventory = inventory

    def display_ui(self):
        """
        Display the current state of the UI on the PyGame screen.
        """
        # Display Health Bar
        health_text = f"Health: {self.health}/{self.max_health}"
        health_surface = self.font.render(health_text, True, (255, 255, 255))
        self.screen.blit(health_surface, (20, 20))

        # Display Score
        score_text = f"Score: {self.score}"
        score_surface = self.font.render(score_text, True, (255, 255, 255))
        self.screen.blit(score_surface, (20, 50))

        # Display Inventory
        inventory_text = f"Inventory: {', '.join(self.inventory)}"
        inventory_surface = self.font.render(inventory_text, True, (255, 255, 255))
        self.screen.blit(inventory_surface, (20, 80))

# Example usage (commented out)
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# font = pygame.font.Font(None, 36)
# game_ui = GameUI(screen, font)
# game_ui.update_health(7)
# game_ui.update_score(150)
# game_ui.update_inventory(['Pickaxe', 'Gold Ore'])
# game_ui.display_ui()
# pygame.quit()
