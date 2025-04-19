import pygame
import cv2
import os
from core.game import Game
image_path = os.path.join('C:\\Users\\romeo\\Documents\\GitHub\\Twin-Pics\\assets\\images\\player.png')
image = cv2.imread(image_path)
if image is None:
    print("Error")
else:
    pass
if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Twin Pics")
    Game().run()
    pygame.quit()