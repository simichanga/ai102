import pygame
from settings import *
from utils import display_message, draw_snake, generate_food_position

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 25)
        self.score_font = pygame.font.SysFont("Arial", 35)

        self.reset_game()

    def reset_game(self):
        self.game_over = False
        self.game_close = False

        self.x1 = WINDOW_WIDTH // 2
        self.y1 = WINDOW_HEIGHT // 2
        self.x1_change = 0
        self.y1_change = 0

        self.snake_list = []
        self.snake_length = 1

        self.foodx, self.foody = generate_food_position(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_BLOCK)

    def display_score(self):
        score_text = f"Score: {self.snake_length - 1}"
        display_message(self.screen, self.score_font, score_text, YELLOW, (10, 10))
    
    def show_menu(self):
        menu = True
        while menu:
            self.screen.fill(BLUE)
            display_message(self.screen, self.font, "Snake Game - Press ENTER to Start", YELLOW, (WINDOW_WIDTH / 6, WINDOW_HEIGHT / 3))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    menu = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    menu = False

    def pause_game(self):
        paused = True
        display_message(self.screen, self.font, "Game Paused. Press P to Resume.", YELLOW, (WINDOW_WIDTH / 6, WINDOW_HEIGHT / 3))
        pygame.display.update()
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    paused = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = False


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pause the game
                    self.pause_game()
                if event.key == pygame.K_LEFT and self.x1_change == 0:
                    self.x1_change = -SNAKE_BLOCK
                    self.y1_change = 0
                elif event.key == pygame.K_RIGHT and self.x1_change == 0:
                    self.x1_change = SNAKE_BLOCK
                    self.y1_change = 0
                elif event.key == pygame.K_UP and self.y1_change == 0:
                    self.x1_change = 0
                    self.y1_change = -SNAKE_BLOCK
                elif event.key == pygame.K_DOWN and self.y1_change == 0:
                    self.x1_change = 0
                    self.y1_change = SNAKE_BLOCK


    def update_snake(self):
        # Update the snake's position
        self.x1 += self.x1_change
        self.y1 += self.y1_change

        # Wrap around the edges of the screen
        if self.x1 >= WINDOW_WIDTH:
            self.x1 = 0
        elif self.x1 < 0:
            self.x1 = WINDOW_WIDTH - SNAKE_BLOCK

        if self.y1 >= WINDOW_HEIGHT:
            self.y1 = 0
        elif self.y1 < 0:
            self.y1 = WINDOW_HEIGHT - SNAKE_BLOCK

        # Add the new head position to the snake
        snake_head = [self.x1, self.y1]
        self.snake_list.append(snake_head)

        # Remove the tail if the snake has grown
        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]

        # Check for collision with itself
        for segment in self.snake_list[:-1]:
            if segment == snake_head:
                self.game_close = True
    
    def adjust_speed(self):
        """Adjust the snake's speed based on its length."""
        speed = SNAKE_SPEED + (self.snake_length // 5)  # Increase speed every 5 points
        return speed



    def check_food_collision(self):
        if self.x1 == self.foodx and self.y1 == self.foody:
            self.foodx, self.foody = generate_food_position(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_BLOCK)
            self.snake_length += 1

    def game_over_screen(self):
        self.screen.fill(BLUE)
        display_message(
            self.screen,
            self.font,
            "You Lost! Press R to Restart or Q to Quit",
            RED,
            (WINDOW_WIDTH / 6, WINDOW_HEIGHT / 3),
        )
        self.display_score()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                self.game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.game_over = True
                    self.game_close = False
                elif event.key == pygame.K_r:
                    self.reset_game()


    def run(self):
        while not self.game_over:
            if self.game_close:
                self.game_over_screen()
            else:
                self.handle_events()
                self.update_snake()
                self.check_food_collision()

                self.screen.fill(BLUE)
                pygame.draw.rect(self.screen, GREEN, [self.foodx, self.foody, SNAKE_BLOCK, SNAKE_BLOCK])
                draw_snake(self.screen, BLACK, SNAKE_BLOCK, self.snake_list)
                self.display_score()

                pygame.display.update()
                self.clock.tick(self.adjust_speed())

        pygame.quit()