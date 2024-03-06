# game_ui.py

class GameUI:
    def __init__(self):
        """
        Initialize the game's user interface.
        """
        # Placeholder for UI elements like health bar, score display, etc.
        self.health_bar = "Health: [||||||||||]"
        self.score_display = "Score: 0"
        self.inventory_display = "Inventory: []"

    def update_health(self, health):
        """
        Update the health bar display.

        :param health: Integer representing the player's current health.
        """
        max_health = 10  # Assuming max health is 10 for simplicity
        health_bar_length = int((health / max_health) * 10)
        self.health_bar = "Health: [" + "|" * health_bar_length + " " * (10 - health_bar_length) + "]"

    def update_score(self, score):
        """
        Update the score display.

        :param score: Integer representing the player's current score.
        """
        self.score_display = f"Score: {score}"

    def update_inventory(self, inventory):
        """
        Update the inventory display.

        :param inventory: List representing the player's current inventory.
        """
        inventory_str = ', '.join(inventory)
        self.inventory_display = f"Inventory: [{inventory_str}]"

    def display_ui(self):
        """
        Display the current state of the UI.
        """
        print(self.health_bar)
        print(self.score_display)
        print(self.inventory_display)

# Example usage (commented out)
# game_ui = GameUI()
# game_ui.update_health(7)
# game_ui.update_score(150)
# game_ui.update_inventory(['Pickaxe', 'Gold Ore'])
# game_ui.display_ui()
