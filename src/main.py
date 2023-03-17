
import pygame
import GameObject as Objects
from WindowRenderer import WindowRenderer
from Utility import check_button_press, Layers, update_gameobjects


def open_inv():
    print('opened inventory')


def start_attack():
    print('ATTAAACK')


def continue_dungeon():
    print('continued in dungeon')


def use_item():
    print('used item')


if __name__ == "__main__":
    window = WindowRenderer(50, 50)
    window.set_background_color(255, 0, 255)

    # Entities
    Jeffrey = Objects.Player(50, 0, pygame.Rect(425, 455, 100, 100), Layers.ENTITIES)

    # Buttons
    invButton = Objects.UiButton(open_inv, pygame.Rect(700, 550, 100, 100), Layers.UI),
    attButton = Objects.UiButton(start_attack, pygame.Rect(125, 550, 450, 100), Layers.UI)
    nxtLvlButton = Objects.UiButton(continue_dungeon, pygame.Rect(425, 20, 150, 50), Layers.UI)

    running = True
    while running:
        update_gameobjects(window)
        window.update()
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                match event:
                    case pygame.K_ESCAPE:
                        running = False

                    # Add more buttons later, perhaps shortcuts?

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    buttons = [obj for obj in Objects.GameObject.instancelist
                               if 'UiButton' in obj.__class__.__name__]  # gets a list of all classes named 'UiButton'

                    check_button_press(buttons, pygame.mouse.get_pos())


pygame.quit()
