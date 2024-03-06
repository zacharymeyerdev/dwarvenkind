# monster.py

class Monster:
    def __init__(self, name, health, attack_power, defense):
        """
        Initialize a new monster.

        :param name: String representing the monster's name.
        :param health: Integer representing the monster's health.
        :param attack_power: Integer representing the monster's attack power.
        :param defense: Integer representing the monster's defense.
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.position = (0, 0)  # Default position, can be set when the monster is spawned

    def move(self):
        """
        Define the logic for monster movement.
        """
        # Placeholder logic for movement, to be expanded based on game design
        # For example, random movement, or moving towards the player
        pass

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

# Example usage (commented out)
# monster = Monster('Goblin', 50, 8, 3)
# player = Player('Dwarf Hero', 100, 10, 5)  # Assuming a Player class exists
# monster.attack(player)
