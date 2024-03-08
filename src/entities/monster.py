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

# monster.py
# Assuming the base Monster class and necessary imports are already defined

class Goblin(Monster):
    def __init__(self, sprite_path, health, attack_power, defense):
        super().__init__("Goblin", sprite_path, health, attack_power, defense)

    def move(self, direction):
        # Goblin can move two squares at a time
        super().move(direction * 2)

class CarrionCrawler(Monster):
    def __init__(self, sprite_path, health, attack_power, defense):
        super().__init__("Carrion Crawler", sprite_path, health, attack_power, defense)
        self.hidden = False

    def hide(self):
        # Hide inside loot spots
        self.hidden = True

class Duergar(Monster):
    def __init__(self, sprite_path, health, attack_power, defense):
        super().__init__("Duergar", sprite_path, health, attack_power, defense)

    def move_and_break_ore(self, direction, map_data):
        # Move and break ores
        new_position = self.position + direction
        # Check if new position has ore and break it
        if map_data[int(new_position.y)][int(new_position.x)] == 'ore':
            map_data[int(new_position.y)][int(new_position.x)] = 'empty'
        self.position = new_position

class CorpseCrawler(Monster):
    def __init__(self, sprite_path, health, attack_power, defense):
        super().__init__("Corpse Crawler", sprite_path, health, attack_power, defense)
        self.size = (2, 2)  # 2x2 tiles big

    def move_and_break_ore(self, direction, map_data):
        # Move and bust through ores
        new_position = self.position + direction
        # Check and break ore in a 2x2 area
        for dx in range(self.size[0]):
            for dy in range(self.size[1]):
                pos_x, pos_y = int(new_position.x + dx), int(new_position.y + dy)
                if map_data[pos_y][pos_x] == 'ore':
                    map_data[pos_y][pos_x] = 'empty'
        self.position = new_position

class Dragon(Monster):
    def __init__(self, sprite_path, health, attack_power, defense):
        super().__init__("Dragon", sprite_path, health, attack_power, defense)

    def breathe_fire(self, target_positions):
        # Breathe fire in a cone
        # Damage or affect targets in `target_positions`
        pass

class Drow(Monster):
    def __init__(self, sprite_path, health, attack_power, defense):
        super().__init__("Drow", sprite_path, health, attack_power, defense)

    def ranged_attack(self, target):
        # Ranged attack logic
        pass

class LivingShroom(Monster):
    def __init__(self, sprite_path, health, attack_power, defense):
        super().__init__("Living Shroom", sprite_path, health, attack_power, defense)
        self.tandem = False

    def cooperate(self, other_shrooms):
        # Work in tandem with other living shrooms
        self.tandem = True
        # Cooperation logic with `other_shrooms`
        pass

class ShroomSovereign(Monster):
    def __init__(self, sprite_path, health, attack_power, defense):
        super().__init__("Shroom Sovereign", sprite_path, health, attack_power, defense)
        self.controlled_shrooms = []

    def control_shrooms(self, shrooms):
        # Control actions of living shrooms
        self.controlled_shrooms = shrooms
        # Intelligent control logic over `shrooms`
        pass

# Note: These are basic structures and behaviors for each monster type.
# Actual implementation will depend on your game design and logic.


# Example usage (commented out)
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# monster = Monster('Goblin', 'path/to/goblin_sprite.png', 50, 8, 3)
# monster.move(pygame.math.Vector2(1, 0))  # Move right
# monster.draw(screen)
# pygame.quit()
