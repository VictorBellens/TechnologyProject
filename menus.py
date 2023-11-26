import pygame

import pygame
import characters


def draw_button(screen, text, font, button_color, text_color, x, y, width, height):
    # Draw button rectangle
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, button_color, button_rect)

    # Render the text
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)

    # Blit the text onto the screen
    screen.blit(text_surface, text_rect)

    return button_rect


def show_start_menu(screen, button_color):
    # Define colors
    button_color = (100, 100, 100)  # Gray color for button
    text_color = (255, 255, 255)    # White color for text
    background_color = (0, 0, 0)     # Black color for background

    # Fill background
    screen.fill(background_color)

    # Set up font
    font = pygame.font.Font(None, 74)  # You can replace None with a font file path

    # Define button properties
    button_width = 250
    button_height = 100
    button_x = (screen.get_width() - button_width) / 2
    button_y = (screen.get_height() - button_height) / 2

    # Draw the button and get its rect
    button_rect = draw_button(screen, "Start Game", font, button_color, text_color, button_x, button_y, button_width, button_height)

    return button_rect


def draw_text_centered(screen, text, font, color, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(screen.get_width() / 2, y))
    screen.blit(text_surface, text_rect)


def load_and_scale_image(image_path, width, height):
    try:
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (width, height))
        return image
    except pygame.error as e:
        print(f"Error loading image {image_path}: {e}")
        return None


def show_character_menu(screen):
    font = pygame.font.SysFont(None, 55)
    color_black = (0, 0, 0)
    draw_text_centered(screen, 'Choose Character', font, color_black, 50)

    char_images = [load_and_scale_image(char["image"], 100, 100) for char in characters.characters]
    button_rects = []

    for i, img in enumerate(char_images):
        if img is not None:
            x = 100 + i * (100 + 10)  # 100px image width + 10px padding
            y = 150  # Fixed y position for all character images
            screen.blit(img, (x, y))
            rect = pygame.Rect(x, y, 100, 100)  # Assuming images are scaled to 100x100
            button_rects.append(rect)
        else:
            # Handle the case when the image is None
            print(f"Image for character {characters.characters[i]['name']} is not available.")

    return button_rects
