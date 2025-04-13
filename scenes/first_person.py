import pygame
from objects.player import Player
from core.config import TEXT_COLOR

class FirstPersonScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Courier", 22)
        self.input = ""
        self.log = ["Ты очнулся в номере мотеля в Твин Пиксе..."]
        self.player = Player()
        # картинка мотеля + музыка на старом радио


    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                command = self.input.strip().lower()
                if command:
                    self.log.append(f"> {command}")
                    result = self.player.act(command)
                    self.log.append(result)
                self.input = ""
            elif event.key == pygame.K_BACKSPACE:
                self.input = self.input[:-1]
            else:
                self.input += event.unicode

    def update(self, dt):
        pass

    def draw(self):
        y = 20
        for line in self.log[-15:]:
            rendered = self.font.render(line, True, TEXT_COLOR)
            self.screen.blit(rendered, (20, y))
            y += 28
        input_surface = self.font.render("> " + self.input, True, TEXT_COLOR)
        self.screen.blit(input_surface, (20, 560))
