# map_generator.py
import random
from tile import Tile

class MapGenerator:
    def __init__(self, width, height, tile_size):
        """
        Initialize the MapGenerator with a specific map size and tile size.

        :param width: Width of the map in tiles.
        :param height: Height of the map in tiles.
        :param tile_size: Size of each tile (width and height in pixels).
        """
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tile_images = {
            'rock': 'path/to/rock_image.png',
            'empty': 'path/to/empty_image.png',
            'ore': 'path/to/ore_image.png',
            'staircase': 'path/to/staircase_image.png',
            'water': 'path/to/water_image.png',
            'lava': 'path/to/lava_image.png'
        }

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
        tile_type = random.choice(['rock', 'empty', 'ore', 'staircase', 'water', 'lava'])
        passable = tile_type not in ['rock', 'lava']
        effect = None  # Define effects for certain tiles
        resource_quantity = random.randint(0, 10) if tile_type == 'ore' else 0
        image_path = self.tile_images[tile_type]

        return Tile(tile_type, image_path, passable, effect, resource_quantity)

    def draw_map(self, surface):
        """
        Draw the map on the given PyGame surface.

        :param surface: The PyGame surface to draw the map on.
        """
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                tile_position = (x * self.tile_size, y * self.tile_size)
                tile.draw(surface, tile_position)

# Example usage (commented out)
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# map_gen = MapGenerator(10, 10, 32)  # 32 pixels per tile
# game_map = map_gen.generate_map()
# map_gen.draw_map(screen)
# pygame.quit()
