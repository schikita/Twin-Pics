import pygame
import cv2
import os
from core.game import Game
image_path = os.path.join('C:\\Users\\romeo\\Documents\\GitHub\\Twin-Pics\\assets\\images\\player.png')
image = cv2.imread(image_path)
if image is None:
    print("Error")
else:
    cv2.imshow("Success", image)
if __name__ == "__main__":
    pygame.init()
    Game().run()
    pygame.quit()