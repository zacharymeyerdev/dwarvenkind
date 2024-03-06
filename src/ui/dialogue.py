# dialogue.py

class DialogueManager:
    def __init__(self, dialogues):
        """
        Initialize the Dialogue Manager.

        :param dialogues: Dictionary mapping character names to their dialogues.
        """
        self.dialogues = dialogues

    def get_dialogue(self, character_name):
        """
        Get the dialogue for a specific character.

        :param character_name: Name of the character.
        :return: List of dialogues for the character.
        """
        return self.dialogues.get(character_name, ["I have nothing to say."])

    def add_dialogue(self, character_name, new_dialogue):
        """
        Add a new dialogue line for a character.

        :param character_name: Name of the character.
        :param new_dialogue: The new dialogue line to add.
        """
        if character_name not in self.dialogues:
            self.dialogues[character_name] = []

        self.dialogues[character_name].append(new_dialogue)

# Example usage (commented out)
# dialogues = {
#     'NPC1': ['Hello, adventurer!', 'Have you seen the dragon?'],
#     'NPC2': ['Welcome to our village.']
# }
# dialogue_manager = DialogueManager(dialogues)
# print(dialogue_manager.get_dialogue('NPC1'))
# dialogue_manager.add_dialogue('NPC3', 'Beware of the goblins in the forest.')
