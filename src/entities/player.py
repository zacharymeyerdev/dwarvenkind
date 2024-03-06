# player.py

class Player:
    def __init__(self, name, health=100, attack_power=10, defense=5, score=0):
        """
        Initialize a new player character.

        :param name: String representing the player's name.
        :param health: Integer representing the player's health.
        :param attack_power: Integer representing the player's attack power.
        :param defense: Integer representing the player's defense.
        :param score: Integer representing the player's score.
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.score = score
        self.inventory = []  # List to store player's items
        self.position = (0, 0)  # Player starts at position (0, 0)

    def move(self, direction):
        """
        Move the player in a given direction.

        :param direction: String ('up', 'down', 'left', 'right') indicating the movement direction.
        """
        x, y = self.position
        if direction == 'up':
            self.position = (x, y-1)
        elif direction == 'down':
            self.position = (x, y+1)
        elif direction == 'left':
            self.position = (x-1, y)
        elif direction == 'right':
            self.position = (x+1, y)

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

# Example usage (commented out)
# player = Player('Dwarf Hero')
# player.move('up')
# player.mine_ore(5)
