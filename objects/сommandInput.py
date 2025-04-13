import pygame

class CommandInput:
    def __init__(self):
        self.text = ""
        self.font = pygame.font.SysFont("Courier", 24)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return self.text
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        return None

    def draw(self, screen):
        surface = self.font.render("> " + self.text, True, (255, 255, 255))
        screen.blit(surface, (20, 540))
