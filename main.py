import pygame
import os
from settings import WIDTH, HEIGHT, GREY, WHITE, BUTTON_SPACING, LEVEL_COUNT
from game_object import GameObject, Button

pygame.init() #start pygame
pygame.mixer.init() #sound

STATE_MAIN_MENU = 1
STATE_LEVEL_MENU = 2
STATE_GAME = 3
FPS = 30

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('my little game')
CLOCK = pygame.time.Clock()

game_state = STATE_MAIN_MENU
main_menu_sprites = pygame.sprite.Group()
play_button = Button("PLAY", WIDTH / 2, HEIGHT / 2 - 50, 200, 50, STATE_LEVEL_MENU)
exit_button = Button("EXIT", WIDTH / 2, HEIGHT / 2 + 50, 200, 50, 'quit')
main_menu_sprites.add(play_button, exit_button)

level_menu_sprites = pygame.sprite.Group()
def setup_level_menu():
    start_y = HEIGHT / 2 - (LEVEL_COUNT * BUTTON_SPACING) / 2
    for i in range(1, LEVEL_COUNT + 1):
        level_name = f"Level {i}"
        y_pos = start_y + (i -1) * BUTTON_SPACING
        level_action = (STATE_GAME, i)
        
        button = Button(text=level_name, x=WIDTH / 2, y=y_pos, WIDTH=200, HEIGHT=40, action=level_action)
        level_menu_sprites.add(button)

setup_level_menu()

all_sprites = pygame.sprite.Group()
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'Human_Soldier_Polearm_Idle-Sheet.png')).convert()
player = GameObject(image=player_img)
all_sprites.add(player)

current_level = 0

running = True
while running:
    CLOCK.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_state == STATE_MAIN_MENU and event.type == pygame.MOUSEBUTTONDOWN:
            for button in main_menu_sprites:
                action = button.check_click(mouse_pos)
                if action:
                    if action == 'quit':
                        running = False
                    else:
                        game_state = action
        elif game_state == STATE_LEVEL_MENU:
            for button in level_menu_sprites:
                action = button.check_click(mouse_pos)
                if action:
                    game_state, level_num = action
                    current_level = level_num

    SCREEN.fill((GREY))

    if game_state == STATE_MAIN_MENU:
        main_menu_sprites.draw(SCREEN)
    elif game_state == STATE_LEVEL_MENU:
        level_menu_sprites.draw(SCREEN)
    elif game_state == STATE_GAME:
        all_sprites.update()
        all_sprites.draw(SCREEN)
    
    pygame.display.flip()

pygame.quit()