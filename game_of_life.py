import pygame
from sys import exit


class Cell:
    def __init__(self, x, y, size):
        # Any value stored on `self` is instance data
        self.x = x
        self.y = y
        self.size = size
        self.alive = False

    def get_color(self):
        if self.alive:
            return "White"
        return "Black"

    def toggle_life(self):
        self.alive = not self.alive
        return self

    def draw_rect(self, screen):
        pygame.draw.rect(
            screen,
            self.get_color(),
            (self.x * self.size, self.y * self.size, self.size, self.size),
        )

    def __str__(self):
        return f"Cell at ({self.x}, {self.y}), Size: {self.size}, Alive: {self.alive}"


# Initilize pygame
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Of Life")
clock = pygame.time.Clock()

# Initilize cells
cell_size = screen_width / 100
cell_dic = {}
for x in range(-100, 201):
    for y in range(-100, 201):
        cell_dic[(x, y)] = Cell(x, y, cell_size)


# Utility functions
def pos_to_cell(pos) -> Cell:
    key = (int(pos[0] / cell_size), int(pos[1] / cell_size))
    return cell_dic[key]


def alive_neighbours(cell_instance) -> int:
    num_alive = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            num_alive += cell_dic[(cell_instance.x + i, cell_instance.y + j)].alive

    return num_alive


def apply_rules(cell_instance):
    if cell_instance.alive:
        if alive_neighbours(cell_instance) < 2 or alive_neighbours(cell_instance) > 3:
            return cell_instance
    else:
        if alive_neighbours(cell_instance) == 3:
            return cell_instance


running = False

while True:
    cells_to_draw = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            cell = pos_to_cell(event.pos)
            cell.toggle_life()
            cell.draw_rect(screen)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running

    cells_toggle_life = []
    if running:
        time_since_move = pygame.time.get_ticks()
        for x in range(-50, 151):
            for y in range(-50, 151):
                cell = apply_rules(cell_dic[(x, y)])
                if cell is not None:
                    cells_toggle_life.append(cell)

        for cell in cells_toggle_life:
            cells_to_draw.append(cell.toggle_life())

    for cell in cells_to_draw:
        cell.draw_rect(screen)

    pygame.display.update()
    clock.tick(20)
