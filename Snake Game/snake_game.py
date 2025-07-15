from tkinter import *
from tkinter import ttk, messagebox
import pygame
import random
import os
import json

# Game constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50
BODY_PARTS = 3
SPEED = 100
score = 0
high_score = 0
direction = "down"
is_paused = False
time_survived = 0
timer_running = False
lives = 3
sound_enabled = True
obstacle_coords = []
OBSTACLE_COUNT = 10
collision_handled = False

# Theme colors
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
OBSTACLE_COLOR = "#555555"

THEMES = {
    "Light": {
        "snake": "#00AA00",
        "food": "#FF0000",
        "background": "#FFFFFF",
        "obstacle": "#888888"
    },
    "Dark": {
        "snake": "#00FF00",
        "food": "#FF0000",
        "background": "#000000",
        "obstacle": "#555555"
    },
    "Neon": {
        "snake": "#00FFFF",
        "food": "#FF00FF",
        "background": "#1A1A1A",
        "obstacle": "#6666FF"
    }
}

SAVE_FILE = "savegame.json"

def load_high_score():
    global high_score
    if os.path.exists("highscore.txt"):
        try:
            with open("highscore.txt", "r") as f:
                high_score = int(f.read())
        except:
            high_score = 0
    else:
        high_score = 0

def save_high_score():
    with open("highscore.txt", "w") as f:
        f.write(str(high_score))

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for _ in range(BODY_PARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        while True:
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            if [x, y] not in snake.coordinates and [x, y] not in obstacle_coords:
                break
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def generate_obstacles():
    global obstacle_coords
    obstacle_coords = []
    canvas.delete("obstacle")
    for _ in range(OBSTACLE_COUNT):
        while True:
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            if [x, y] not in obstacle_coords and [x, y] not in snake.coordinates:
                obstacle_coords.append([x, y])
                canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=OBSTACLE_COLOR, tag="obstacle")
                break

def next_turn(snake, food):
    global collision_handled
    if is_paused:
        window.after(SPEED, next_turn, snake, food)
        return
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        if sound_enabled:
            eat_sound.play()
        global score, high_score
        score += 1
        if score > high_score:
            high_score = score
            save_high_score()
        update_status_label()
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        if not collision_handled:
            collision_handled = True
            handle_life_loss()
    else:
        collision_handled = False
        window.after(SPEED, next_turn, snake, food)

def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    for part in snake.coordinates[1:]:
        if x == part[0] and y == part[1]:
            return True
    for ox, oy in obstacle_coords:
        if x == ox and y == oy:
            return True
    return False

def handle_life_loss():
    global lives
    lives -= 1
    update_status_label()
    if sound_enabled:
        gameover_sound.play()
    if lives <= 0:
        game_over()
    else:
        messagebox.showinfo("Life Lost", f"You have {lives} lives remaining.")
        restart_game()

def change_direction(new_direction):
    global direction
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

def toggle_pause(event=None):
    global is_paused
    is_paused = not is_paused

def toggle_sound():
    global sound_enabled
    sound_enabled = not sound_enabled
    sound_btn.config(text=f"Sound: {'On' if sound_enabled else 'Off'}")

def restart_game(event=None):
    global snake, food, direction, is_paused, timer_running
    canvas.delete(ALL)
    direction = 'down'
    is_paused = False
    timer_running = True
    update_status_label()
    snake = Snake()
    generate_obstacles()
    food = Food()
    start_timer()
    next_turn(snake, food)

def game_over():
    global timer_running
    timer_running = False
    canvas.delete(ALL)
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2, font=('consolas', 60), text="GAME OVER", fill="red")
    messagebox.showinfo("Game Over", f"Final Score: {score}")

def start_timer():
    global time_survived, timer_running
    if not timer_running:
        return
    time_survived += 1
    update_status_label()
    window.after(1000, start_timer)

def update_status_label():
    label.config(text=f"Score: {score} | High Score: {high_score} | Time: {time_survived}s | Lives: {lives}")

def start_game():
    global SNAKE_COLOR, FOOD_COLOR, BACKGROUND_COLOR, SPEED, canvas, label, snake, food, OBSTACLE_COLOR
    global time_survived, timer_running, lives, collision_handled, score

    theme = theme_var.get()
    difficulty = difficulty_var.get()
    colors = THEMES[theme]
    SNAKE_COLOR = colors['snake']
    FOOD_COLOR = colors['food']
    BACKGROUND_COLOR = colors['background']
    OBSTACLE_COLOR = colors['obstacle']
    SPEED = {"Easy": 150, "Medium": 100, "Hard": 50}[difficulty]

    menu_frame.destroy()
    label_frame = Frame(window)
    label_frame.pack(fill=X)
    global label
    label = Label(label_frame, text="", font=('consolas', 18), anchor='w')
    label.pack(side=LEFT, padx=10, pady=5)
    global sound_btn
    sound_btn = Button(label_frame, text=f"Sound: {'On' if sound_enabled else 'Off'}", command=toggle_sound)
    sound_btn.pack(side=RIGHT, padx=10)

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

    time_survived = 0
    lives = 3
    score = 0
    collision_handled = False
    timer_running = True
    update_status_label()
    start_timer()
    snake = Snake()
    generate_obstacles()
    food = Food()
    next_turn(snake, food)

window = Tk()
window.title("Snake Game")
window.resizable(False, False)
load_high_score()
pygame.mixer.init()
eat_sound = pygame.mixer.Sound("assets/eat.wav")
gameover_sound = pygame.mixer.Sound("assets/gameover.wav")

menu_frame = Frame(window, padx=20, pady=20)
menu_frame.pack()
Label(menu_frame, text="🐍 SNAKE GAME", font=("consolas", 50)).pack(pady=10)
theme_var = StringVar(value="Dark")
difficulty_var = StringVar(value="Medium")
Label(menu_frame, text="Choose Theme:", font=("consolas", 20)).pack(pady=5)
ttk.Combobox(menu_frame, textvariable=theme_var, values=list(THEMES.keys()), font=("consolas", 15), state="readonly").pack()
Label(menu_frame, text="Choose Difficulty:", font=("consolas", 20)).pack(pady=10)
ttk.Combobox(menu_frame, textvariable=difficulty_var, values=["Easy", "Medium", "Hard"], font=("consolas", 15), state="readonly").pack()
Button(menu_frame, text="Start Game", font=("consolas", 16), command=start_game).pack(pady=30)
Label(menu_frame, text="Use Arrow Keys to move\nP = Pause | R = Restart", font=("consolas", 12)).pack(pady=10)

window.bind('<Left>', lambda e: change_direction('left'))
window.bind('<Right>', lambda e: change_direction('right'))
window.bind('<Up>', lambda e: change_direction('up'))
window.bind('<Down>', lambda e: change_direction('down'))
window.bind('<p>', toggle_pause)
window.bind('<r>', restart_game)
window.update()
x = (window.winfo_screenwidth() // 2) - (GAME_WIDTH // 2)
y = (window.winfo_screenheight() // 2) - (GAME_HEIGHT // 2)
window.geometry(f"{GAME_WIDTH + 50}x{GAME_HEIGHT + 50}+{x}+{y}")
window.mainloop()
