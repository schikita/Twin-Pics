import pygame
import cv2
import os
import numpy as np
from objects.player import Player
from core.config import TEXT_COLOR

image_path = os.path.join('assets//images//motel-room.png')
music_path = os.path.join('assets', 'sound', 'motel-music.mp3')

#Hello
class FirstPersonScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Courier", 22)
        self.input = ""
        self.log = ["Ты очнулся в номере мотеля в Твин Пиксе...\n"
        "1. Осмотреться\n"
        "2. Выглянуть в окно\n"
        "3. Выйти на улицу\n"
        "4. ..."]
        self.player = Player()
        self.background = self._load_background(image_path)
        self._setup_music()


    def _setup_music(self):
        if os.path.exists(music_path):
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)
        else:
            print(f'Музыка не найдена: {music_path}')

    def _load_background(self, path):
        image = cv2.imread(path)
        if image is None:
            raise FileExistsError(f'Фоновое изображение  не найдено: {image_path}')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        surf = pygame.surfarray.make_surface(image)
        rotated = pygame.transform.rotate(surf, -90)
        return pygame.transform.scale(rotated, self.screen.get_size())
    

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
        self.screen.blit(self.background, (0 , 0))
        pygame.draw.rect(self.screen,(0,0,0),(0,450,800,600))
        for line in self.log[-15:]:
            rendered = self.font.render(line, True, TEXT_COLOR)
            self.screen.blit(rendered, (20, y))
            y += 28
        input_surface = self.font.render("> " + self.input, True, TEXT_COLOR)
        self.screen.blit(input_surface, (20, 560))
