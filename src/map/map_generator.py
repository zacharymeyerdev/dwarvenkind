# map_generator.py
import random
from tile import Tile

class MapGenerator:
    def __init__(self, width, height):
        """
        Initialize the MapGenerator with a specific map size.

        :param width: Width of the map.
        :param height: Height of the map.
        """
        self.width = width
        self.height = height

    def generate_map(self):
        """
        Generate a new map with random tiles.

        :return: 2D list representing the map.
        """
        map_data = [[None for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                map_data[y][x] = self.generate_tile(x, y)

        return map_data

    def generate_tile(self, x, y):
        """
        Generate a single tile at a given position.

        :param x: X-coordinate of the tile.
        :param y: Y-coordinate of the tile.
        :return: A Tile object.
        """
        # Example tile generation logic - can be expanded
        tile_type = random.choice(['rock', 'empty', 'ore', 'staircase', 'water', 'lava'])
        passable = tile_type not in ['rock', 'lava']
        effect = None  # Define effects for certain tiles
        resource_quantity = random.randint(0, 10) if tile_type == 'ore' else 0

        return Tile(tile_type, passable, effect, resource_quantity)

# Example usage (commented out)
# map_gen = MapGenerator(10, 10)
# game_map = map_gen.generate_map()
