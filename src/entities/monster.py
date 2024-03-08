# monster.py
import pygame

class Monster:
    def __init__(self, name, sprite_path, health, attack_power, defense):
        """
        Initialize a new monster with PyGame.

        :param name: String representing the monster's name.
        :param sprite_path: Path to the monster's sprite image.
        :param health: Integer representing the monster's health.
        :param attack_power: Integer representing the monster's attack power.
        :param defense: Integer representing the monster's defense.
        """
        self.name = name
        self.sprite = pygame.image.load(sprite_path)
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.position = pygame.math.Vector2(0, 0)  # Default position, can be set when the monster is spawned

    def move(self, direction):
        """
        Move the monster in a given direction using PyGame.

        :param direction: Vector2 representing the movement direction.
        """
        self.position += direction

    def attack(self, target):
        """
        Attack a target.

        :param target: The target to attack (usually the player).
        """
        damage = self.attack_power - target.defense
        target.health -= max(0, damage)  # Ensure damage isn't negative

    def is_alive(self):
        """
        Check if the monster is still alive.

        :return: Boolean indicating whether the monster is alive.
        """
        return self.health > 0

    def draw(self, surface):
        """
        Draw the monster on the given PyGame surface.

        :param surface: The PyGame surface to draw the monster on.
        """
        surface.blit(self.sprite, (self.position.x, self.position.y))

# Example usage (commented out)
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# monster = Monster('Goblin', 'path/to/goblin_sprite.png', 50, 8, 3)
# monster.move(pygame.math.Vector2(1, 0))  # Move right
# monster.draw(screen)
# pygame.quit()
