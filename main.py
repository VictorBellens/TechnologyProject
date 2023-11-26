import pygame
from player import Player
from level import Level
from menus import show_start_menu, show_character_menu
import characters

# Constants for game states
START_MENU = 'start_menu'
CHARACTER_SELECTION = 'character_selection'
MAIN_GAME = 'main_game'


def game_loop(screen):
    clock = pygame.time.Clock()
    running = True
    current_state = START_MENU
    start_button_rect = None  # This will be set by the show_start_menu function
    character_button_rects = []
    button_color = (100, 100, 100)  # Default button color
    kitchen_level = Level('sprites/map1.png', scale_factor=3)  # Replace with actual path
    player_character = None
    character_selected = False

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if start_button_rect is not None before using collidepoint
                if current_state == START_MENU and start_button_rect and start_button_rect.collidepoint(event.pos):
                    current_state = CHARACTER_SELECTION
                elif current_state == CHARACTER_SELECTION:
                    for idx, rect in enumerate(character_button_rects):
                        if rect.collidepoint(event.pos):
                            # Use the actual path from the characters list
                            character_image_path = characters.characters[idx]["image"]
                            player_character = Player(100, 100, character_image_path)
                            character_selected = True
                            current_state = MAIN_GAME
                # Check if start_button_rect is not None before using collidepoint
                if current_state == START_MENU and start_button_rect and start_button_rect.collidepoint(pygame.mouse.get_pos()):
                    button_color = (150, 150, 150)  # Lighter gray for hover
                else:
                    button_color = (100, 100, 100)  # Original gray color

        # Update game state
        screen.fill((255, 255, 255))  # Clear screen
        if current_state == START_MENU:
            start_button_rect = show_start_menu(screen, button_color)
        elif current_state == CHARACTER_SELECTION:
            character_button_rects = show_character_menu(screen)
        elif current_state == MAIN_GAME:
            if character_selected:
                kitchen_level.draw(screen)
                player_character.draw(screen)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    player_character.update('up')
                if keys[pygame.K_DOWN]:
                    player_character.update('down')
                if keys[pygame.K_LEFT]:
                    player_character.update('left')
                if keys[pygame.K_RIGHT]:
                    player_character.update('right')

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
