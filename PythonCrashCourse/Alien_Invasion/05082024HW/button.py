import pygame

class Button:

    def __init__(self, arc, msg):
        self.screen = arc.screen
        self.screen_rect = self.screen.get_rect()

        self.button_color = (200, 200, 200)
        self.text_color = (20, 20, 20)
        self.font = pygame.font.SysFont(None, 50)

        self.rect = pygame.Rect(0, 0, 200, 100)
        self.rect.center = self.screen_rect.center

        self._write_msg(msg)

    def _write_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    
    

# def easy_button_click(self):
