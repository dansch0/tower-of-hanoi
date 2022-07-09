
from game.notification import Notification


class NotificationManager:
    def __init__(self, game) -> None:

        self.notifications_stack = []

        self.add_notification(Notification("Bem-vindo, Daniel!", game))

    def update(self):
        
        if(len(self.notifications_stack)>0):

            self.notifications_stack[0].draw()

            if(self.notifications_stack[0].finished):
                self.notifications_stack.pop(0)

    def add_notification(self, notification):

        for noti in self.notifications_stack:
            if(noti.text == notification.text):
                return

        self.notifications_stack.append(notification)