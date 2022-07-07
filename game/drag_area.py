class DragArea:

    def __init__(self, pos_x, pos_y, width, height, game):
        
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.game = game
        self.item_stack = []

    def update(self):

        self.check_draggable_items()

        self.set_items_pos()

        ##self.game.render.render_rect(self.pos_x, self.pos_y, self.width, self.height, (200, 30, 30, 0.2))

    def set_items_pos(self):

        stack_length = len(self.item_stack)

        if(stack_length == 0):
            return

        item_count = 1

        for item in self.item_stack:

            if(item.pressed):
                continue

            item.pos_x = self.pos_x + (self.width/2) - (item.image_width/2)
            item.pos_y = self.pos_y + (self.height) - (item.image_height*item_count)+(4*item_count)-4

            item_count += 1

    def check_draggable_items(self):

        stack_length = len(self.item_stack)

        if(stack_length == 0):
            return

        for index, item in enumerate(self.item_stack, start=0):   # default is zero

            if(index == len(self.item_stack)-1):
                item.draggable = True
                continue

            item.draggable = False

    def stack_item(self, item):

        if(len(self.item_stack) == 0):
            self.item_stack.append(item)
            return True
        
        last_local_size = self.item_stack[len(self.item_stack)-1].item_size
        new_size = item.item_size

        # Check item size
        if(last_local_size < new_size):
            return False

        self.item_stack.append(item)
        return True

    def pop_item(self):
        self.item_stack.pop()