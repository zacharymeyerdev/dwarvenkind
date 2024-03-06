# tile.py

class Tile:
    def __init__(self, tile_type, passable, effect=None, resource_quantity=0):
        """
        Initialize a new tile.

        :param tile_type: String representing the type of tile (e.g., 'rock', 'ore', 'staircase').
        :param passable: Boolean indicating whether the tile can be walked on.
        :param effect: Any special effect that occurs when interacting with the tile (e.g., damage, healing).
        :param resource_quantity: For resource tiles (like ore), the quantity of the resource.
        """
        self.tile_type = tile_type
        self.passable = passable
        self.effect = effect
        self.resource_quantity = resource_quantity

    def interact(self, player):
        """
        Define interactions that occur when a player interacts with this tile.
        
        :param player: The player character interacting with the tile.
        """
        # Example interaction logic:
        if self.tile_type == 'ore':
            # Mining ore logic
            if self.resource_quantity > 0:
                # Update player score/resources
                player.mine_ore(self.resource_quantity)
                # Deplete the ore
                self.resource_quantity -= 1

        elif self.tile_type == 'staircase':
            # Logic for descending to the next level
            player.descend_level()

        elif self.tile_type == 'trap':
            # Trigger a trap effect
            if self.effect:
                self.effect(player)

        # Additional interaction types can be added here

    def is_passable(self):
        """
        Check if the tile is passable.

        :return: Boolean indicating passability.
        """
        return self.passable

# Example usage (commented out)
# player = Player(...)  # Assuming a Player class exists
# tile = Tile('ore', True, resource_quantity=5)
# tile.interact(player)
