# npc.py
import pygame
import random

class NPC:
    def __init__(self, name, sprite_path, dialogue):
        """
        Initialize a new non-player character (NPC) with PyGame.

        :param name: String representing the NPC's name.
        :param sprite_path: Path to the NPC's sprite image.
        :param dialogue: List of strings representing the NPC's dialogue.
        """
        self.name = name
        self.sprite = pygame.image.load(sprite_path)
        self.dialogue = dialogue
        self.position = pygame.math.Vector2(0, 0)  # Default position, can be set when the NPC is placed on the map

    def speak(self):
        """
        Trigger a dialogue with the NPC.

        :return: A string from the NPC's dialogue.
        """
        # Example: return a random dialogue line
        return random.choice(self.dialogue)

    def give_quest(self):
        """
        Assign a quest to the player.

        :return: Details of the quest.
        """
        # Placeholder for quest logic
        # Example: return a quest object or description
        return "Find the lost artifact in the depths of the cavern."

    def trade(self):
        """
        Handle trade interactions with the player.

        :return: Details of trade items or actions.
        """
        # Placeholder for trade logic
        # Example: return available items for trade
        return "Available items: pickaxe, health potion, map fragment."

    def draw(self, surface):
        """
        Draw the NPC on the given PyGame surface.

        :param surface: The PyGame surface to draw the NPC on.
        """
        surface.blit(self.sprite, (self.position.x, self.position.y))

# Example usage (commented out)
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# npc = NPC('Wise Elder', 'path/to/wise_elder_sprite.png', ['Welcome, traveler!', 'Beware the depths below.'])
# npc.draw(screen)
# pygame.quit()
