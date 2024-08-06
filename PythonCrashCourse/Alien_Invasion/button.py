import pygame.font

from time import sleep

class Button:
    # Class that builds button

    def __init__(self, ai_game, msg):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (200, 230, 200)
        self.text_color = (0, 10, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0,0, self.width, self.height)
        # self.rect.center = self.screen_rect.center
        self.message_text = msg

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def button_positioning(self, flag, x=0, y=0):
        if flag == None:
            self.rect.center = (x, y)
        elif flag == "center":
            self.rect.center = self.screen_rect.center
        self._prep_msg(self.message_text)

    def button_clicked(self):
        self.button_color = (255, 10, 10)
        self.text_color = (240, 240, 240)
        self._prep_msg(self.message_text)
        

    def button_unclicked(self):
        self.button_color = (200, 230, 200)
        self.text_color = (0, 10, 0)
        self._prep_msg(self.message_text)