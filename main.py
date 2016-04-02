"""
Istanbul Technical University
VOGK GameJam Gaming Project.
Game theme is "Cloud".
"""

import sys
import math
import random
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def roint(num):
    return int(round(num))

class SaveTheVampire(object):
    """
    Main game class.
    """

    
    def __init__(self, canvas_size):
        """
        Initializing required main game and pygame values. 
        """

        self.width, self.height = canvas_size              # Set width and height to canvas size.
        self.screen = pygame.display.set_mode(canvas_size) # Set screen surface
        self.clock = pygame.time.Clock()                   # TPS of the main game loop
        self.game_time = 0                                 # Game time in seconds

        self.sun_angle = -30
        self.sun_pos = [roint(self.width / 2 + 760 * math.cos(math.radians(self.sun_angle)) - 200),
                        roint(self.height + 500 * math.sin(math.radians(self.sun_angle)) - 120)]
        self.sun_image = pygame.image.load("sun.png")

        self.player_pos = [500,  400]
        self.player_image = pygame.image.load("player.png")

        self.lightning_comp = -60
        self.lightning = [50, 50, 50]
        self.level_base_lightning = [50, 50, 50]

        self.timer_queue = []
        self.timer_queue.append(self.timer(self.update_sun, 1))
        self.timer_queue.append(self.timer(self.update_lightning, 1))
        #self.timer_queue.append()
        #self.timer_queue.append()

        pygame.init()


    def main(self):
        """
        The main game method includes the main loop.
        """

        while True:
            self.clock.tick(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()

            self.game_time += 1

            #mouse = pygame.mouse.get_pos()
            #print mouse
            self.apply_timer()
            self.draw_gameplay()

    ################################### Mouse Handlers ############################################

    def menu_click():
        pass

    ################################### Drawing Methods ###########################################

    def draw_menu(self):
        pass

    def draw_gameplay(self):

        self.screen.fill(self.lightning)

        self.screen.blit(self.sun_image, self.sun_pos)
        self.screen.blit(self.player_image, self.player_pos)

        pygame.display.flip()


    ################################### Status Updates ############################################

    def timer(self, method, interval):
        """
        Create timer values for methods that are applied over time intervals.
        """

        apply_time = self.game_time % interval  
        return (method, apply_time, interval)

    def apply_timer(self):
        """
        Apply everything in the timer queue, keeping the intervals.
        """

        for method, apply_time, interval in self.timer_queue:
            if self.game_time % interval == apply_time:            
                method()

    def update_sun(self):
        """
        Updates sun position and the lightning of the map.
        """

        self.sun_angle -= 1
        self.sun_angle %= 360


        self.sun_pos[0] = roint(self.width / 2 + 760 * math.cos(math.radians(self.sun_angle)) - 120)
        self.sun_pos[1] = roint(self.height + 500 * math.sin(math.radians(self.sun_angle)) - 120)

    def update_lightning(self):

        if self.lightning_comp < 55:
            self.lightning_comp += 1

            x = self.lightning_comp**3
            y = self.lightning_comp
            
            self.lightning[0] = self.level_base_lightning[0] - roint(y)
            self.lightning[1] = self.level_base_lightning[1] - roint(y)
            self.lightning[2] = self.level_base_lightning[2] - roint(y)
 

    def move_vampire(self):
        pass




if __name__ == "__main__":
    game = SaveTheVampire((1000, 600))
    game.main()