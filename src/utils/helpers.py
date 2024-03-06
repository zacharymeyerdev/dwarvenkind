# helpers.py

def calculate_distance(pos1, pos2):
    """
    Calculate the Euclidean distance between two points.

    :param pos1: Tuple (x, y) representing the first position.
    :param pos2: Tuple (x, y) representing the second position.
    :return: Float representing the distance.
    """
    return ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5

def clamp(value, min_value, max_value):
    """
    Clamp a value between a minimum and maximum value.

    :param value: The value to clamp.
    :param min_value: The minimum allowed value.
    :param max_value: The maximum allowed value.
    :return: The clamped value.
    """
    return max(min_value, min(value, max_value))

def direction_to_vector(direction):
    """
    Convert a direction (e.g., 'up', 'down') to a vector.

    :param direction: String representing the direction.
    :return: Tuple (dx, dy) representing the direction vector.
    """
    if direction == 'up':
        return (0, -1)
    elif direction == 'down':
        return (0, 1)
    elif direction == 'left':
        return (-1, 0)
    elif direction == 'right':
        return (1, 0)
    else:
        return (0, 0)

# Example usage (commented out)
# distance = calculate_distance((0, 0), (3, 4))
# clamped_value = clamp(15, 0, 10)
# direction_vector = direction_to_vector('up')
