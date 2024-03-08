# helpers.py
import pygame

def calculate_distance(pos1, pos2):
    """
    Calculate the Euclidean distance between two points using PyGame.

    :param pos1: Tuple (x, y) representing the first position.
    :param pos2: Tuple (x, y) representing the second position.
    :return: Float representing the distance.
    """
    return pygame.math.Vector2(pos1).distance_to(pygame.math.Vector2(pos2))

def clamp(value, min_value, max_value):
    """
    Clamp a value between a minimum and maximum value using PyGame.

    :param value: The value to clamp.
    :param min_value: The minimum allowed value.
    :param max_value: The maximum allowed value.
    :return: The clamped value.
    """
    return max(min_value, min(value, max_value))

def direction_to_vector(direction):
    """
    Convert a direction (e.g., 'up', 'down') to a vector using PyGame.

    :param direction: String representing the direction.
    :return: Tuple (dx, dy) representing the direction vector.
    """
    directions = {
        'up': pygame.math.Vector2(0, -1),
        'down': pygame.math.Vector2(0, 1),
        'left': pygame.math.Vector2(-1, 0),
        'right': pygame.math.Vector2(1, 0)
    }
    return directions.get(direction, pygame.math.Vector2(0, 0))

# Example usage (commented out)
# distance = calculate_distance((0, 0), (3, 4))
# clamped_value = clamp(15, 0, 10)
# direction_vector = direction_to_vector('up')
