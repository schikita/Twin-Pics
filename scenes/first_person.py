import pygame
import cv2
import os
import numpy as np
from objects.player import Player
from core.config import TEXT_COLOR

image_path = os.path.join('assets', 'images', 'motel-room.png')
music_path = os.path.join('assets', 'sound', 'motel-music.mp3')

class FirstPersonScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Courier", 22)
        self.input = ""
        self.log = [
            'Ты очнулся в номере мотеля в Твин Пиксе...',
            "1. Осмотреться ",
            "2. Выглянуть в окно ",
            "3. Выйти на улицу ", 
            "4. ..."
        ]
        self.player = Player()
        self.background = self._load_background(image_path)

        self._setup_music()

        self.cursor_visible = True
        self.cursor_timer = 0.0
        self.cursor_interval = 0.5

        self.input_locked = False
        self.input_lock_timer = 0.0
        self.input_lock_duration = 1.5

        self.typing_text = ""
        self.typing_progress = 0
        self.typing_speed = 30
        self.typing_active = False

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
            raise FileExistsError(f'Фоновое изображение не найдено: {image_path}')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        surf = pygame.surfarray.make_surface(image)
        rotated = pygame.transform.rotate(surf, -90)
        return pygame.transform.scale(rotated, self.screen.get_size())

    def handle_event(self, event):
        if self.input_locked:
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                command = self.input.strip().lower()
                if command:
                    self.log.clear()  # ОЧИЩАЕМ лог полностью
                    self.log.append(f"> {command}")
                    result = self.player.act(command)
                    if result:
                        self.typing_text = result
                        self.typing_progress = 0
                        self.typing_active = True

                self.input = ""  
                self.input_locked = True
            elif event.key == pygame.K_BACKSPACE:
                self.input = self.input[:-1]
            else:
                self.input += event.unicode

    def update(self, dt):
        self.cursor_timer += dt
        if self.cursor_timer >= self.cursor_interval:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0.0

        if self.input_locked:
            self.input_lock_timer += dt
            if self.input_lock_timer >= self.input_lock_duration:
                self.input_locked = False
                self.input_lock_timer = 0.0

        # <-- Блок печатания должен быть отдельно, а не внутри input_locked!
        if self.typing_active:
            self.typing_progress += self.typing_speed * dt
            num_chars = int(self.typing_progress)
            if num_chars >= len(self.typing_text):
                self.log.append(self.typing_text)
                self.typing_text = ""
                self.typing_active = False
            else:
                if not self.log or self.log[-1] != self.typing_text[:num_chars]:
                    if self.log and self.log[-1].startswith(self.typing_text[:num_chars - 1]):
                        self.log[-1] = self.typing_text[:num_chars]
                    else:
                        self.log.append(self.typing_text[:num_chars])


    def draw(self):
        y = 450
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 450, 800, 600))
    
        for line in self.log[-15:]:
            rendered = self.font.render(line, True, TEXT_COLOR)
            self.screen.blit(rendered, (20, y))
            y += 22

        # Инициализируем input_text правильно
        if not self.input_locked:
            input_text = "> " + self.input
            if self.cursor_visible:
                input_text += "|"
        
            input_surface = self.font.render(input_text, True, TEXT_COLOR)
            self.screen.blit(input_surface, (20, 560))
        else:
            # Ввод заблокирован — не рисуем ничего!
            pass