# dialogue.py
import pygame

class DialogueManager:
    def __init__(self, dialogues, font, screen):
        """
        Initialize the Dialogue Manager with PyGame.

        :param dialogues: Dictionary mapping character names to their dialogues.
        :param font: PyGame font for rendering text.
        :param screen: PyGame screen where dialogues will be displayed.
        """
        self.dialogues = dialogues
        self.font = font
        self.screen = screen
        self.current_dialogue = None

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

    def display_dialogue(self, character_name):
        """
        Display the dialogue of a character on the screen.

        :param character_name: Name of the character.
        """
        self.current_dialogue = self.get_dialogue(character_name)

        for line in self.current_dialogue:
            text_surface = self.font.render(line, True, (255, 255, 255))
            # Position the text on the screen (example: bottom of the screen)
            y_position = self.screen.get_height() - 50
            self.screen.blit(text_surface, (20, y_position))
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait for 2 seconds before displaying next line

# Example usage (commented out)
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# font = pygame.font.Font(None, 36)
# dialogues = {
#     'NPC1': ['Hello, adventurer!', 'Have you seen the dragon?'],
#     'NPC2': ['Welcome to our village.']
# }
# dialogue_manager = DialogueManager(dialogues, font, screen)
# dialogue_manager.display_dialogue('NPC1')
# pygame.quit()
