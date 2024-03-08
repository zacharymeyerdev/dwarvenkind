# tile.py

import pygame

class Tile:
    def __init__(self, tile_type, image_path, passable, effect=None, resource_quantity=0):
        """
        Initialize a new tile with PyGame.

        :param tile_type: String representing the type of tile (e.g., 'rock', 'ore', 'staircase').
        :param image_path: Path to the image representing the tile.
        :param passable: Boolean indicating whether the tile can be walked on.
        :param effect: Any special effect that occurs when interacting with the tile (e.g., damage, healing).
        :param resource_quantity: For resource tiles (like ore), the quantity of the resource.
        """
        self.tile_type = tile_type
        self.image = pygame.image.load(image_path)
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

    def draw(self, surface, position):
        """
        Draw the tile on the given surface at the specified position.

        :param surface: The PyGame surface to draw on.
        :param position: Tuple (x, y) representing the position to draw the tile.
        """
        surface.blit(self.image, position)

    def is_passable(self):
        """
        Check if the tile is passable.

        :return: Boolean indicating passability.
        """
        return self.passable

# Example usage (commented out)
# Initialize PyGame (required for image loading)
# pygame.init()
# player = Player(...)  # Assuming a Player class exists
# tile = Tile('ore', 'path/to/ore_image.png', True, resource_quantity=5)
# tile.interact(player)
# pygame.quit()
