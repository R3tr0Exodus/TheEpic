import pygame


class GameObject:
    sprite: pygame.Surface = None
    rect: pygame.Rect

    def __init__(self, rect, sprite=None):
        self.sprite = sprite
        self.rect = rect

    def update(self):
        pass

    def start(self):
        pass


class Item(GameObject):
    pass


class Buff(GameObject):
    pass


class Entity(GameObject):
    health: int = 0
    baseHealth: int = 0
    dmg: int = 0
    baseDmg: int = 0
    sprite: pygame.Surface = None
    rect: pygame.Rect = None

    def super__init__(self, baseHealth, baseDmg, rect, spritePath: str="/sprites/Jerry_sprite",):
        self.health = baseHealth
        self.baseHealth = baseHealth
        self.dmg = baseDmg
        self.baseDmg = baseDmg
        self.rect = rect
        self.sprite = pygame.image.load(spritePath)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        print("ouchie!")


class Player(Entity):
    __inventory: list = []
    attackItem: Item = None
    defensiveItem: Item = None
    attackBuffs: Buff = []
    defensiveBuffs: Buff = []

    def get_inventory(self) -> list:
        return self.__inventory

    def add_inventory(self, item: Item):
        self.__inventory.append(item)

    def use_item(self):
        pass


class UiButton(GameObject):
    pass