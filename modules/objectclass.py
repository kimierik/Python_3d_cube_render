#code
import math
import pygame
from . import config


class object3d:

    def __init__(self,objectlist):#wtf is happening why is every self.obj linked to each other
        self.obj=[(),(),(),(),(),(),(),()]

        self.fcube=[(),(),(),(),(),(),(),()]
        #dont twice i dont remember why

        for i in range(len(objectlist)):
            self.obj[i] = objectlist[i] 



    def matrixmulti(self,multipmatrix,cordmatrix):
        #this matrix can only calculate if the following are true
        #multimatrix will always be x row 3 collum
        #cord matrix will always be 3row 1 collum
        #only in cord matrix only input (x,y,z)touple in that format
        returncords=[0,0,0]
        #x,y,z=cordmatrix
        iterator=0
        for mrow in multipmatrix:#mrow is touple and each () in the given matrix
            for i in range(len(mrow)):#i is every number in the touple

                returncords[iterator]+=(mrow[i]*cordmatrix[i])  
                #multiplier always gives us the right answer

            iterator+=1

        return returncords

   



    def rotatez(self,angle):
        rotatezmatrix=[
                (math.cos(angle),-math.sin(angle),0),
                (math.sin(angle),math.cos(angle),0),
                (0,0,1)]
        for i in range(len(self.obj)):
            x,y,z=self.matrixmulti(rotatezmatrix,self.obj[i])
            self.obj[i]=[x,y,z]
         
        



    def rotatex(self,angle):
        roratexmatrix=(
        (1,0,0),
        (0,math.cos(angle)  ,-math.sin(angle)   ),
        (0,math.sin(angle)  ,math.cos(angle)    )
            )
        #print(roratexmatrix)
        for i in range(len(self.obj)):
            #i = number 0-7
            #print(cube[i])
            x,y,z=self.matrixmulti(roratexmatrix,self.obj[i])
            self.obj[i]=[x,y,z]
            


    def rotatey(self,angle):
        rotateymatrix=(
        (math.cos(angle),   0   ,math.sin(angle)),
        (0,                 1,  0),
        (-math.sin(angle),  0   ,math.cos(angle))
            )
        for i in range(len(self.obj)):
            x,y,z=self.matrixmulti(rotateymatrix,self.obj[i])
            self.obj[i]=[x,y,z]


    #render function that does too many things
    def render(self,color):
        a=0
        #magic number. some sorf of an iterator

        for i in range(len(self.obj)):
            x,y,z=self.matrixmulti(config.projectmatrix,self.obj[i])
            self.fcube[i]=[x+config.width/2,y+config.height/2]
            rect=pygame.Rect(x+config.width/2,y+config.height/2,5,5)
            #pygame.draw.rect(win,color,rect)
        

        #a really shit way to draw the lines of a cube
        for i in range(int(len(self.fcube)/2)):
            a=i+1
            if i+1==4:
                a=0
            pygame.draw.line(config.win,color,self.fcube[i],self.fcube[a])


        for i in range(4,len(self.fcube)):
            a=i+1
            if i+1==8:
                a=4
            pygame.draw.line(config.win,color,self.fcube[i],self.fcube[a])


        for i in range(int(len(self.fcube)/2)):
            pygame.draw.line(config.win,color,self.fcube[i],self.fcube[i+4])


