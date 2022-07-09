from random import randint
import pygame
from game.drag_area import DragArea
from game.drag_item import DragItem
from game.notification import Notification, NotificationPosition, NotificationType


class DragManager:

    def __init__(self, game):

        self.game = game
        self.drag_areas_pack = []
        self.num_of_movements = 0
        self.start_pole_index = randint(0, 2) # Randomizing pole begin

        # Adding all the areas
        self.add_drag_area(DragArea(0, 350, 426, 300, game))
        self.add_drag_area(DragArea(426, 350, 426, 300, game))
        self.add_drag_area(DragArea(426*2, 350, 426, 300, game))

        self.load_rings(game.rings_amount)


    def load_rings(self, num_of_rings):
        for i in range(num_of_rings):
            self.drag_areas_pack[self.start_pole_index].stack_item(DragItem(num_of_rings-i-1, "Ring"+str(num_of_rings-i), self.game))


    def check_win(self):
        for i,area in enumerate(self.drag_areas_pack):
            if(i == self.start_pole_index):
                continue

            if(len(area.item_stack) == self.game.rings_amount):
                return True
        return False


    def update(self, game):
		
        for area in self.drag_areas_pack:
            area.update()

            for item in area.item_stack:

                # If true, the user dropped a ring in somewhere
                if(item.draw()):

                    # Lets check if its on a DragArea
                    area_dropped = self.get_area_dropped()

                    # If not, bleh
                    if(not area_dropped):
                        continue
                    
                    # lets check if the dropped area is te same origin area
                    if(area_dropped == area):
                        continue

                    # Yess, lets check if we can stack this ring
                    if(area_dropped.stack_item(item)):

                        area.pop_item()
                        self.num_of_movements +=1

                        if(self.check_win()):
                            game.notification_manager.add_notification(
                                Notification(
                                    "Você Ganhou!", 
                                    game, 
                                    duration_time=8,
                                    position=NotificationPosition.CENTER, 
                                    type=NotificationType.BIG
                                    ))
                    else:
                        game.notification_manager.add_notification(
                            Notification(
                                "Você só pode colocar anéis pequenos em cima dos grandes!", 
                                game))


                        
    def get_area_dropped(self):

        for area in self.drag_areas_pack:
            area_rect = pygame.Rect(area.pos_x, area.pos_y, area.width, area.height)
            mouse_pos = pygame.mouse.get_pos()

            if(area_rect.collidepoint(mouse_pos)):
                return area

        return False


    def add_drag_area(self, dragarea):
        self.drag_areas_pack.append(dragarea)