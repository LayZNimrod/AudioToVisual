import pygame 

# 'clamps' a value to stay within a specific range 
def clamp(min, max, val): 

    if val < min:
        return min
    elif val > max:
        return max
    else:
        return val 

# deals with all the varaibles to create the audio bars 
class Bar:
    def __init__(self, x, y, freq, color, width = 50, min_height = 10,
                 max_height = 100, min_decibel=-80, max_decibel = 0):

        self.x, self.y, self.freq = x,y, freq

        self.color = color 

        self.width, self.min_height, self.max_height = width, min_height, max_height

        self.height = min_height

        self.min_decibel, self.max_decibel, = min_decibel, max_decibel

        self.__decibel_height_ratio = (self.max_height - self.min_height) / (self.max_decibel - self.min_decibel)

    # changes the height and speed of the bars with each frame 
    def update(self, dt, decibel):
        desired_height = decibel * self.__decibel_height_ratio + self.max_height
        speed = (desired_height - self.height)/0.1
        self.height += speed * dt
        self.height = clamp(self.min_height, self.max_height, self.height)
    
    # draws each bar to the screen
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y + self.max_height - self.height, self.width, self.height))


