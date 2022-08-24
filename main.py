#!/bin/python3
import pygame
import math
import random
from modules import stack 
from modules import tools
from modules import config


def main():
    run=True
    angle=0.01
    clock=pygame.time.Clock()

    cube=[
(-50,-50,-50),
(50,-50,-50 ),
(50,50,-50  ),
(-50,50,-50 ),

(-50,-50,50 ),
(50,-50,50  ),
(50,50,50   ),
(-50,50,50  )]


    testcube=stack.cube(cube)
#    tryout=object3(cube)

    #print(matrixmulti(initmat,testmat))
    while run:
        clock.tick(config.fps)



        config.win.fill(config.black)
        #testcube.rotatex(angle*2)
        #testcube.rotatey(angle*random.randint(0,1))
        #testcube.rotatez(angle/math.pi)

        #tryout.rotatez(-angle/math.pi)
        #tryout.rotatex(-angle)
    #    tryout.rotatey(-angle)
        testcube.render()
        testcube.render_wireframe()
        #testcube.render_fill()
        #tryout.render(blue)
        angle+=(0.001/100000)



        #make user input


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False


        pressed=pygame.key.get_pressed()






#this "if" monstrosity checks when buttons are pressed
        
        if pressed[pygame.K_a]:
            testcube.rotatey(-angle)
        if pressed[pygame.K_d]:
            testcube.rotatey(angle)

        if pressed[pygame.K_w]:
            testcube.rotatex(-angle)
        if pressed[pygame.K_s]:
            testcube.rotatex(angle)

        if pressed[pygame.K_q]:
            testcube.rotatez(-angle)
        if pressed[pygame.K_e]:
            testcube.rotatez(angle)
            
        
        if pressed[pygame.K_f]:
            testcube.render_fill()


        pygame.display.update()

    pygame.quit()




if __name__=="__main__":
    main()



