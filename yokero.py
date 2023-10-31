import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((600, 400))
    bg_img = pg.image.load("ex05/fig/pg_bg.jpg")
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type==pg.QUIT: return
        screen.blit(bg_img, [0, 0])
        pg.display.update()
        
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()