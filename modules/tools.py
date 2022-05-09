#code



#calculates area of triangle
def CalculateTriangleArea(p1,p2,p3):
    for i in range(2):
        p1[i]=int(p1[i])
        p2[i]=int(p2[i])
        p3[i]=int(p3[i])
    return abs(( p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]) ) /2)


def matrixmulti(multipmatrix,cordmatrix):
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


