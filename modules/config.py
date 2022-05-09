#pygame init and coingi stuff



import pygame
import math
import random
pygame.init()

width,height=900,600
win=pygame.display.set_mode((width,height))
fps=60
pygame.display.set_caption("3d render practice")

black=(0,0,0)
white =(255,255,255)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
mix1=(255,255,0)
mix2=(0,255,255)
mix3=(255,0,255)


projectmatrix=(
        (1,0,0),
        (0,1,0) )



"""
cube=[
(-50,-50,-50),
(50,-50,-50 ),
(50,50,-50  ),
(-50,50,-50 ),

(-50,-50,50 ),
(50,-50,50  ),
(50,50,50   ),
(-50,50,50  )]
"""
#print(cube[2])



fcube=[(),(),(),(),(),(),(),()]

initmat=(
(53,27,56),
(52,46,-55),
(45,47,76)
        )
testmat=(78,34,48)


