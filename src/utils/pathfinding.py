# pathfinding.py
import pygame
from queue import PriorityQueue

def find_path(start, goal, map_data):
    """
    Find the shortest path from start to goal using PyGame.

    :param start: Tuple (x, y) representing the start position.
    :param goal: Tuple (x, y) representing the goal position.
    :param map_data: 2D list representing the map, where 0 is passable and 1 is an obstacle.
    :return: List of tuples as the path from start to goal.
    """
    def get_neighbors(pos):
        """
        Get neighbors of the current position.

        :param pos: Tuple (x, y).
        :return: List of neighbor positions.
        """
        directions = [pygame.math.Vector2(0, -1), pygame.math.Vector2(0, 1),
                      pygame.math.Vector2(-1, 0), pygame.math.Vector2(1, 0)]  # up, down, left, right
        neighbors = []
        for direction in directions:
            x, y = pos[0] + direction.x, pos[1] + direction.y
            if 0 <= x < len(map_data[0]) and 0 <= y < len(map_data) and map_data[int(y)][int(x)] == 0:
                neighbors.append((x, y))
        return neighbors

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()[1]

        if current == goal:
            break

        for next in get_neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + abs(goal[0] - next[0]) + abs(goal[1] - next[1])
                frontier.put((priority, next))
                came_from[next] = current

    # Reconstruct path
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()  # Reverse path to start-to-goal order
    return path

# Example usage (commented out)
# map_data = [[0, 0, 0, 0, 1], 
#             [1, 1, 0, 1, 1],
#             [0, 0, 0, 0, 0],
#             [1, 0, 1, 1, 0],
#             [0, 0, 0, 0, 0]]
# start = (0, 0)
# goal = (4, 4)
# path = find_path(start, goal, map_data)
