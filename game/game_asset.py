
import pygame

class AssetType:
    IMAGE = 1
    FONT = 2


class GameAsset:

    def __init__(self, name, path, type, font_size, image_scale):
        
        self.name = name
        self.path = path
        self.type = type

        if(type == AssetType.IMAGE):
            self.asset_load = pygame.image.load(path)

            if(image_scale != 1):
                size_x, size_y = self.asset_load.get_size()
                self.asset_load = pygame.transform.scale(self.asset_load, (size_x*image_scale, size_y*image_scale))

        elif(type == AssetType.FONT):
            self.asset_load = pygame.font.Font(path, font_size)