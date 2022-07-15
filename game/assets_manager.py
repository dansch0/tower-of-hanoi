
import pygame

from game.game_asset import *

class AssetsManager:

    assets_pack = []

    def __init__(self) -> None:
        self.load_assets()

    def add_asset(self, name, path, type, font_size=12, image_scale=1) -> None:
        self.assets_pack.append(GameAsset(name, path, type, font_size, image_scale))

    def get_asset(self, name) -> GameAsset:
        for asset in self.assets_pack:
            if(asset.name == name):
                return asset
        return None

    def load_assets(self) -> None:

        # Fonts
        self.add_asset("PixelFont14","fonts/pixel_font.ttf", AssetType.FONT, font_size=14)
        self.add_asset("PixelFont18","fonts/pixel_font.ttf", AssetType.FONT, font_size=18)
        self.add_asset("PixelFont24","fonts/pixel_font.ttf", AssetType.FONT, font_size=24)
        self.add_asset("PixelFont32","fonts/pixel_font.ttf", AssetType.FONT, font_size=32)

        # Images
        self.add_asset("Ground",    "images/ground.png",        AssetType.IMAGE,  image_scale=4)
        self.add_asset("SmallBush", "images/small_bush.png",    AssetType.IMAGE,  image_scale=4)
        self.add_asset("BigBush",   "images/big_bush.png",      AssetType.IMAGE,  image_scale=4)
        self.add_asset("Pole",      "images/pole.png",          AssetType.IMAGE,  image_scale=4)
        self.add_asset("Ring1",     "images/ring1.png",         AssetType.IMAGE,  image_scale=4)
        self.add_asset("Ring2",     "images/ring2.png",         AssetType.IMAGE,  image_scale=4)
        self.add_asset("Ring3",     "images/ring3.png",         AssetType.IMAGE,  image_scale=4)
        self.add_asset("Ring4",     "images/ring4.png",         AssetType.IMAGE,  image_scale=4)
        self.add_asset("Ring5",     "images/ring5.png",         AssetType.IMAGE,  image_scale=4)
        self.add_asset("Ring6",     "images/ring6.png",         AssetType.IMAGE,  image_scale=4)
    
