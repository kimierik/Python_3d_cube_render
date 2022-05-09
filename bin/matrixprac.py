#!/bin/python3
import pygame
import math
import random
from modules import objectclass
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


    testcube=objectclass.object3d(cube)
#    tryout=object3(cube)

    #print(matrixmulti(initmat,testmat))
    while run:
        clock.tick(config.fps)



        win.fill(config.black)
        testcube.rotatex(angle*2)
        testcube.rotatey(angle*random.randint(0,1))
        testcube.rotatez(angle/math.pi)

        #tryout.rotatez(-angle/math.pi)
        #tryout.rotatex(-angle)
    #    tryout.rotatey(-angle)
        testcube.render(config.white)
        #tryout.render(blue)
        angle+=(0.001/100000)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False





    pygame.quit()




if __name__=="__main__":
    main()



