import math 
import pygame
import random


pygame.init()
width,height=600, 600

win=pygame.display.set_mode((width,height))

pointlist=[]


black=(0,0,0)
white=(255,255,255)


def CalculateTriangleArea(p1,p2,p3):
    return abs(( p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]) ) /2)
#this is a lil spagetti
#index 0 shouopd be x and index 1 shoulkd always be y
#send in touples
        #re check if this is anywhere near correct to be acvcurate(taken from internet)

        

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class triangle:
    def __init__(self, p1, p2, p3):
        self.pointlist=[p1,p2,p3]
        self.p1=p1
        self.p2=p2
        self.p3=p3
        #self.points are only defined to test fill
        self.area = CalculateTriangleArea( (p1.x,p1.y) , (p2.x,p2.y) , (p3.x,p3.y))

    def render(self):
        for i in self.pointlist:
            rect=pygame.Rect(i.x,i.y,10,10)
            pygame.draw.rect(win,white,rect)




    def connect(self):#makes lines to connet points
        for index in range(len(self.pointlist)):
            a1=self.pointlist[index]
            if index==2:
                a2=self.pointlist[0]
            else:
                a2=self.pointlist[index+1]
            #a1 and a2 are names for the two points that we are calculating

            
            dx=a2.x-a1.x
            dy=a2.y-a1.y
            #we can do the angle method and iterate sqrt(dx²+dy²) and use the iteration as hypotenuse then multiply it with the angle
            #this is not the fastest way to draw but idc

            try:
                angle= math.atan(dy/dx)
            except:
                angle=math.pi+math.pi/2
            #this try except is to avoid division by 0 event
            #if dx is 0 this means it is directly below the first point




            if dx <0:
                angledif=math.pi/2+angle
                angle=angledif+math.pi/2
            #multipleying angle with the iteration of hypotenuse does not work without this
            #if dx is negative it returns unusable numbers for this calculation
            

            hypotenuse=math.sqrt(pow(dx,2)+pow(dy,2))
            #this is the distance between a1 and a2
            #print(a1.x,a1.y," ",a2.x,a2.y," ",angle)
            for i in range(int(hypotenuse)):
                xn=math.cos(angle)*i
                yn=math.sin(angle)*i
                win.set_at((a1.x+int(xn),a1.y+int(yn)),white)
            #draw line across the length of hypotenuse according to angle
        



    #get smallest and largest x value in pointilst
    def get_x_range(self):
        return(min(self.p1.x,self.p2.x,self.p3.x) , max(self.p1.x,self.p2.x,self.p3.x))


    def get_y_range(self):
        return(min(self.p1.y,self.p2.y,self.p3.y) , max(self.p1.y,self.p2.y,self.p3.y))

    #fill triangle with col argument
    def fill(self, col):
        #get smallest x and y
        minx,maxx=self.get_x_range()
        miny,maxy=self.get_y_range()

        #algo to check if point is in triangle
        for x in range(minx,maxx):
            for y in range(miny,maxy):
                a1=CalculateTriangleArea( (x,y) , (self.p2.x,self.p2.y) , (self.p3.x,self.p3.y) )
                a2=CalculateTriangleArea( (x,y) , (self.p1.x,self.p1.y) , (self.p3.x,self.p3.y) )
                a3=CalculateTriangleArea( (x,y) , (self.p1.x,self.p1.y) , (self.p2.x,self.p2.y) )
                if self.area ==(a1+a2+a3):
                    win.set_at((x,y),col)




def main():
    win.fill(black) 
    run=True
    p1=point(random.randint(0,width),random.randint(0,height))
    p2=point(random.randint(0,width),random.randint(0,height))
    p3=point(random.randint(0,width),random.randint(0,height))
    t1=triangle(p1,p2,p3)
    #manually assigning points and giving them to rtriangle class

    while run:
        
        #t1.render()
#        t1.connect()
        t1.fill(white)
        #attempt to fill with barycentric algo
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        

        pygame.display.update()
        
    pygame.quit()









if __name__=="__main__":
    main()


