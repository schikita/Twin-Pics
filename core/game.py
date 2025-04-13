# core/game.py

import pygame
from core.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG_COLOR
from scenes.first_person import FirstPersonScene

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Twin Peaks: Quest")
        self.clock = pygame.time.Clock()
        self.scene = FirstPersonScene(self.screen)

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(FPS) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.scene.handle_event(event)

            self.scene.update(dt)
            self.screen.fill(BG_COLOR)
            self.scene.draw()
            pygame.display.flip()
