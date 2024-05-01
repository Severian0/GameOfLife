import time
import pygame
import numpy as np

BG = (10, 10, 10)
GRID = (60, 60, 60)
DEAD = (170, 170, 170)
ALIVECOL = (255, 255, 255)

def update(screen, cells, dimens, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for i, j in np.ndindex(cells.shape):
        alive = np.sum (cells[i-1:i+2, j-1:j+2]) - cells[i, j]
        colour = BG if cells [i, j] == 0 else ALIVECOL

        if cells[i, j] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    colour = DEAD
            elif 2 <= alive <= 3:
                updated_cells[i, j] = 1
                if with_progress:
                    colour = ALIVECOL
        else:
            if alive == 3:
                updated_cells[i, j] = 1
                if with_progress:
                    colour = ALIVECOL

        pygame.draw.rect(screen, colour, (j * dimens, i * dimens, dimens - 1, dimens - 1))

    return updated_cells



def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((60, 80))
    screen.fill(GRID)
    update(screen, cells, 10)
    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
                if event.key == pygame.K_e:
                    pos = pygame.mouse.get_pos()
                    cells[pos[1] // 10, pos[0] // 10] = 0
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()
            
        screen.fill(GRID)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)


if __name__ == '__main__':
    main()
