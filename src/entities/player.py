# player.py
import pygame

class Player:
    def __init__(self, name, sprite_path, health=100, attack_power=10, defense=5, score=0):
        """
        Initialize a new player character with PyGame.

        :param name: String representing the player's name.
        :param sprite_path: Path to the player's sprite image.
        :param health: Integer representing the player's health.
        :param attack_power: Integer representing the player's attack power.
        :param defense: Integer representing the player's defense.
        :param score: Integer representing the player's score.
        """
        self.name = name
        self.sprite = pygame.image.load(sprite_path)
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.score = score
        self.inventory = []  # List to store player's items
        self.position = pygame.math.Vector2(0, 0)  # Player starts at position (0, 0)

    def move(self, direction):
        """
        Move the player in a given direction using PyGame.

        :param direction: Vector2 representing the movement direction.
        """
        self.position += direction

    def attack(self, target):
        """
        Attack a target.

        :param target: The target to attack (e.g., a monster).
        """
        # Example attack logic
        damage = self.attack_power - target.defense
        target.health -= max(0, damage)  # Ensure damage isn't negative

    def mine_ore(self, quantity):
        """
        Mine ore and add points to the player's score.

        :param quantity: The quantity of ore mined.
        """
        self.score += quantity

    def pick_up_item(self, item):
        """
        Add an item to the player's inventory.

        :param item: The item to be picked up.
        """
        self.inventory.append(item)

    def use_item(self, item):
        """
        Use an item from the player's inventory.

        :param item: The item to be used.
        """
        # Example item usage logic (e.g., healing, buffing)
        pass

    def descend_level(self):
        """
        Handle the logic for descending to the next level.
        """
        # Logic for moving to the next level (e.g., increase difficulty, reset map)
        pass

    def draw(self, surface):
        """
        Draw the player on the given PyGame surface.

        :param surface: The PyGame surface to draw the player on.
        """
        surface.blit(self.sprite, (self.position.x, self.position.y))

# Example usage (commented out)
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# player = Player('Dwarf Hero', 'path/to/sprite.png')
# player.move(pygame.math.Vector2(1, 0))  # Move right
# player.draw(screen)
# pygame.quit()
