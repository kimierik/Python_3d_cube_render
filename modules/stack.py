#this migth be broken into more files later
import pygame
import math
from . import config
from . import tools

class point3d:
    def __init__(self,point):
        self.x,self.y,self.z=point
        pass
    def get_info(self):
        return([self.x,self.y,self.z])

    def set_info(self,values):
        self.x=values[0]
        self.y=values[1]
        self.z=values[2]


    def get_2d(self):
        return ([self.x+config.width/2,self.y+config.height/2])



class triangle:
    def __init__(self,p1,p2,p3,color):
        self.color=color
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.area = tools.CalculateTriangleArea( [p1.x,p1.y] , [p2.x,p2.y] , [p3.x,p3.y])

        #make function that fills the triangle with a color gotten from the plane
        #
        #
        #

    def render(self):
        pygame.draw.line(config.win,self.color,self.p1.get_2d(),self.p2.get_2d())
        pygame.draw.line(config.win, self.color,self.p3.get_2d(),self.p2.get_2d())
        pygame.draw.line(config.win, self.color,self.p1.get_2d(),self.p3.get_2d())



    def get_x_range(self):
        return(min(self.p1.x,self.p2.x,self.p3.x) , max(self.p1.x,self.p2.x,self.p3.x))


    def get_y_range(self):
        return(min(self.p1.y,self.p2.y,self.p3.y) , max(self.p1.y,self.p2.y,self.p3.y))

## swap this to pygane native thing since it is probs faster
    def fill(self):
        #get smallest x and y
        minx,maxx=self.get_x_range()
        miny,maxy=self.get_y_range()
        self.area = tools.CalculateTriangleArea( [self.p1.x,self.p1.y] , [self.p2.x,self.p2.y] , [self.p3.x,self.p3.y])

        #algo to check if point is in triangle
        for x in range(int(minx),int(maxx)):
            for y in range(int(miny),int(maxy)):
                a1=tools.CalculateTriangleArea( [x,y] , [self.p2.x,self.p2.y] , [self.p3.x,self.p3.y] )
                a2=tools.CalculateTriangleArea( [x,y] , [self.p1.x,self.p1.y] , [self.p3.x,self.p3.y] )
                a3=tools.CalculateTriangleArea( [x,y] , [self.p1.x,self.p1.y] , [self.p2.x,self.p2.y] )
                if self.area ==a1+a2+a3:
                    config.win.set_at((int(x+config.width/2),int(y+config.height/2)),self.color)











class plane:
    #c refers to corner
    def __init__(self,c1,c2,c3,c4,color):
        self.color=color
        self.cornerlist=[c1,c2,c3,c4]
        self.triangle1=triangle(c1,c2,c3,self.color)
        self.triangle2=triangle(c1,c4,c3,self.color)
        #plane needs a color that is given from cube
        #
        #

    def render_plane(self):
        pygame.draw.line(config.win,self.color, self.cornerlist[0].get_2d(), self.cornerlist[1].get_2d())
        pygame.draw.line(config.win,self.color, self.cornerlist[1].get_2d(), self.cornerlist[2].get_2d())
        pygame.draw.line(config.win,self.color, self.cornerlist[3].get_2d(), self.cornerlist[0].get_2d())
        pygame.draw.line(config.win,self.color, self.cornerlist[2].get_2d(), self.cornerlist[3].get_2d())


    def render_triangle(self):
        self.triangle1.render()
        self.triangle2.render()

    def fill(self):
        self.triangle1.fill()
        self.triangle2.fill()

#returns z cord of center pixel
    def get_centerz(self):
        #xdif=abs(self.cornerlist[0].x-self.cornerlist[2].x)
        #ydif=abs(self.cornerlist[0].x-self.cornerlist[2].y)
        #return [abs(self.cornerlist[0].x+xdif),abs(self.cornerlist[0].y+ydif)]
        zdif=abs(self.cornerlist[0].z-self.cornerlist[2].z)
        return self.cornerlist[0].z+zdif/2


class cube:
    def __init__(self,point_list):
        ##thinking
        #
        self.plane_list=[]
        self.list_of_points=[(),(),(),(),(),(),(),(),]
        for index,points in enumerate(point_list):
            self.list_of_points[index]=point3d(points)
            
        #manually taking values points from the list and making planes out of them

        self.plane1=plane(self.list_of_points[0],self.list_of_points[1],self.list_of_points[2],self.list_of_points[3],config.blue)
        self.plane2=plane(self.list_of_points[4],self.list_of_points[5],self.list_of_points[6],self.list_of_points[7],config.red)
        self.plane3=plane(self.list_of_points[1],self.list_of_points[2],self.list_of_points[6],self.list_of_points[5],config.green)
        self.plane4=plane(self.list_of_points[0],self.list_of_points[3],self.list_of_points[7],self.list_of_points[4],config.mix1)
        self.plane5=plane(self.list_of_points[2],self.list_of_points[3],self.list_of_points[7],self.list_of_points[6],config.mix2)
        self.plane6=plane(self.list_of_points[0],self.list_of_points[1],self.list_of_points[5],self.list_of_points[4],config.mix3)

        self.plane_list=[self.plane1, self.plane2, self.plane3, self.plane4, self.plane5, self.plane6]

        #self.plane_list=[self.plane5]#, self.plane5, self.plane6]

    def rotatez(self,angle):
        rotatezmatrix=[
                (math.cos(angle),-math.sin(angle),0),
                (math.sin(angle),math.cos(angle),0),
                (0,0,1)]

        for i in self.list_of_points:
            x,y,z=tools.matrixmulti(rotatezmatrix,i.get_info())
            i.set_info([x,y,z])

    def rotatex(self,angle):
        rotatexmatrix=(
        (1,0,0),
        (0,math.cos(angle)  ,-math.sin(angle)   ),
        (0,math.sin(angle)  ,math.cos(angle)    )
            )
        #print(roratexmatrix)
        for i in self.list_of_points:
            x,y,z=tools.matrixmulti(rotatexmatrix,i.get_info())
            i.set_info([x,y,z])
            

    def rotatey(self,angle):
        rotateymatrix=(
        (math.cos(angle),   0   ,math.sin(angle)),
        (0,                 1,  0),
        (-math.sin(angle),  0   ,math.cos(angle))
            )


        for i in self.list_of_points:
            x,y,z=tools.matrixmulti(rotateymatrix,i.get_info())
            i.set_info([x,y,z])

    def render(self):
        for i in self.plane_list:
            i.render_plane()
        pass

    def render_wireframe(self):
        for i in self.plane_list:
            i.render_triangle()


    def render_fill(self):
        #sort planelist first
        centers_list=[]

        
        for i in self.plane_list:
            center=i.get_centerz()
            centers_list.append((i,center))
        centers_list.sort(key=(lambda y:y[1]))
        for i in centers_list:
            print(i)
            i[0].fill()




