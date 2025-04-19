import pygame
import cv2
import os
from core.game import Game
image_path = os.path.join('player.png')
image = cv2.imread(image_path)
if image is None:
    print("Error")
else:
    cv2.imshow("Success", image)
if __name__ == "__main__":
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    Game().run()
    pygame.quit()