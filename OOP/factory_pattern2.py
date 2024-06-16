import pygame
import random
from abc import ABC, abstractmethod

# base abstract class
class Shape(ABC):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self,surface):
        pass

# circle class inheriting from shape
class Circle(Shape):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.radius = random.randint(10,50)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    # draw circle on the given surface
    def draw(self,surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y),self.radius)

#rectangle class inheriting from shape
class Rectangle(Shape):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.width = random.randint(10,100)
        self.height = random.randint(10,100)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    # daw rectangle on the given surface
    def draw(self,surface):
        pygame.draw.rect(surface,self.color,(self.x,self.y,self.width,self.height))

# shapefactory for creating shape instances
class ShapeFactory:
    #static method is bound to the class and not the object of the class. 
    #This method can’t access or modify the class state.
    #It is present in a class because it makes sense for the method to be present in class.
    @staticmethod
    def create_shape(context):
        if shape_type=='Circle':
            return Circle(x,y)
        elif shape_type=='Rectangle':
            return Rectangle(x,y)
        else:
            raise ValueError("Invalid Shape Type")

# shape context to hold factory parameters     
class ShapeContext:
    def __init__(self,shape_type,x,y):
        self.shape_type =shape_type
        

# main function to set up and run the game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Random shapes")
    clock = pygame.time.Clock()

    shape_factory = ShapeFactory()
    shapes = []
    running = True

    # main game loop
    while running:
        # process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running == False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                shape_type = random.choice(['Circle','Rectangle'])
                shape = shape_factory.create_shape(shape_type,x,y)
                shapes.append(shape)

        # clear the screen
        screen.fill((255,255,255))
        # draw all the shapes
        for shape in shapes:
            shape.draw(screen)
        
        # update the display
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
