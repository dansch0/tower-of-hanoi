import pygame
from game.drag_area import DragArea
from game.drag_item import DragItem


class DragManager:

    

    def __init__(self, game):

        self.drag_areas_pack = []

        self.num_of_movements = 0

        # Adding all the areas
        self.add_drag_area(DragArea(0, 350, 426, 300, game))
        self.add_drag_area(DragArea(426, 350, 426, 300, game))
        self.add_drag_area(DragArea(426*2, 350, 426, 300, game))

        num_of_rings = game.rings_amount

        for i in range(num_of_rings):
            self.drag_areas_pack[0].stack_item(DragItem(num_of_rings-i-1, "Ring"+str(num_of_rings-i), game))

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
                    else:
                        print("Você não pode colocar uma anel maior em cima de um anel menor!")

                        


    def get_area_dropped(self):

        for area in self.drag_areas_pack:
            area_rect = pygame.Rect(area.pos_x, area.pos_y, area.width, area.height)
            mouse_pos = pygame.mouse.get_pos()

            if(area_rect.collidepoint(mouse_pos)):
                return area

        return False

    def add_drag_area(self, dragarea):
        self.drag_areas_pack.append(dragarea)