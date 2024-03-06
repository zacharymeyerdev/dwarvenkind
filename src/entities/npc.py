# npc.py
import random

class NPC:
    def __init__(self, name, dialogue):
        """
        Initialize a new non-player character (NPC).

        :param name: String representing the NPC's name.
        :param dialogue: List of strings representing the NPC's dialogue.
        """
        self.name = name
        self.dialogue = dialogue
        self.position = (0, 0)  # Default position, can be set when the NPC is placed on the map

    def speak(self):
        """
        Trigger a dialogue with the NPC.

        :return: A string from the NPC's dialogue.
        """
        # Example: return a random dialogue line
        return random.choice(self.dialogue)

    def give_quest(self):
        """
        Assign a quest to the player.

        :return: Details of the quest.
        """
        # Placeholder for quest logic
        # Example: return a quest object or description
        return "Find the lost artifact in the depths of the cavern."

    def trade(self):
        """
        Handle trade interactions with the player.

        :return: Details of trade items or actions.
        """
        # Placeholder for trade logic
        # Example: return available items for trade
        return "Available items: pickaxe, health potion, map fragment."

# Example usage (commented out)
# npc = NPC('Wise Elder', ['Welcome, traveler!', 'Beware the depths below.'])
# dialogue = npc.speak()
# quest = npc.give_quest()
# trade_info = npc.trade()
