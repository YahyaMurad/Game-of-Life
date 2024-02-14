import random
import pygame
import sys

class Board:
    def __init__(self, width, height, state=None):
        self.width = width
        self.height = height

        if state is not None:
            self.board = state
        else:
            self.board = [[0] * width for _ in range(height)]

    def __str__(self):
        res = ""
        for i in range(len(self.board)):
            res += str(self.board[i]) + "\n"

        return res
    
    def randomize(self):
        count_1 = (self.width * self.height) // 10
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.height // 3 <= j <= self.height // 1.5  and self.width // 3 <= i <= self.width // 1.5:
                    num = random.randint(0, 1)
                    if num == 1 and count_1 > 0:
                        count_1 -= 1
                        self.board[i][j] = 1
                    else:
                        self.board[i][j] = 0
                else:
                    self.board[i][j] = 0

    def update(self):
        new_board = [[0] * len(self.board[0]) for _ in range(len(self.board))]

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                neighbors = self.count_neighbors(i, j)
                if self.board[i][j] == 1:
                    new_board[i][j] = 1 if 2 <= neighbors <= 3 else 0
                else:
                    new_board[i][j] = 1 if neighbors == 3 else 0

        self.board = new_board

    def count_neighbors(self, i, j):
        neighbors = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for direction in directions:
            new_pixel = (i + direction[0], j + direction[1])
            
            if 0 <= new_pixel[0] < self.width and 0 <= new_pixel[1] < self.height:
                if self.board[new_pixel[0]][new_pixel[1]] == 1:
                    neighbors += 1

        return neighbors

    def display(self):
        pygame.init()

        cell_size = 20
        screen_size = (len(self.board[0]) * cell_size, len(self.board) * cell_size)
        screen = pygame.display.set_mode(screen_size)

        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update()

            screen.fill((0, 0, 0))

            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    color = (0, 0, 0) if self.board[i][j] == 0 else (255, 255, 255)
                    pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

            pygame.display.flip()
            clock.tick(5)