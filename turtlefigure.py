from turtle import *
import math

class spirograph:
    # class static variables
    debug = True

    # constructor
    def __init__(self, angle, length):
        if self.debug:
            print("I'm in innit")
        #initialise the class variables
        self.angle = angle
        self.length = length

    def drawSpiroGraph(self):
        if self.debug:
            print("I'm in draw")
        begin_fill()
        while True:
            forward(self.angle)
            left(self.length)
            if abs(pos()) < 1:
                break
        #end_fill()
        done()

#Uncomment for test run
#spiro = spirograph(200, 100)
#spiro.drawSpiroGraph()

class binarytree:
     
     def drawBinaryTree(self,angle,length):
          self.angle = angle
          self.length =length

          if angle==0 or length<2 :
               return
          #endif
          forward(length)
          left(45)
          self.drawBinaryTree(angle-1, length/2)
          right(90)
          self.drawBinaryTree(angle-1, length/2)
          left(45)
          backward(length)
          
     #end tree
#end class

          
#Comment out to run          
#b = binarytree()
#b.drawBinaryTree(350,50)

class spike:

    # class static variables
    spikeRatio = .75
        
    def drawSpike(self, angle, length):
    
        self.angle = angle
        self.length = length

        effectiveAngle = angle % 360
        effectiveRotation = 360 - effectiveAngle
        requiredRotations = 360// effectiveRotation

        for i in range(requiredRotations):
            forward(length*self.spikeRatio)
            right(angle)
            backward(length)
    
#Uncomment for test run
#spk = spike()
#spk.drawSpike(336, 100)

class fernTree:

    def drawFern(self, angle, length):
        if angle==0 or length<2:
            return
        # endif
        forward (0.3*length);
        left(55);
        
        self.drawFern(angle-1, length/2);
        right(55);
        forward (0.7*length);
        right(40);

        self.drawFern(angle-1, length/2);
        left(40);
        forward(length);
        left(5);

        self.drawFern(angle-1, 0.8*length);
        right(5);
        backward(2*length);
    #end
        
#Uncomment for test run
#fern = fernTree()
#fern.drawFern(38,199)

class snowFlake:
    
    def koch(self, angle, length):
        if length<2 or angle==0:
            forward(length)
            return
    
        #endif
        self.koch(angle-1,length/3)
        left(60)
        self.koch(angle-1,length/3)
        right(120)
        self.koch(angle-1,length/3)
        left(60)
        self.koch(angle-1,length/3);
    #end koch


    def drawFlake(self, angle, length):
        for g in range (3) :
            self.koch(angle,length)
            left(120)
    # endfor
# end flake


#flake = snowFlake()
#flake.drawFlake(333,167)

class antiSnowFlake:
    
    def koch(self, angle, length):
        if length<2 or angle==0:
            forward(length)
            return
    
        #endif
        self.koch(angle-1,length/3)
        left(60)
        self.koch(angle-1,length/3)
        right(120)
        self.koch(angle-1,length/3)
        left(60)
        self.koch(angle-1,length/3);
    #end koch


    def drawAntiFlake(self, angle, length):
        for g in range (3) :
            self.koch(angle,length)
            right(120)
    # endfor
# end antiFlake

#Uncomment for test run
#antiFlake = antiSnowFlake()
#antiFlake.drawAntiFlake(33,67)

class circleCeption:

    def drawCircleCeption(self,angle, length):

        if length<2 or angle<0:
            return

        effectiveAngle = angle % 360
        effectiveRotation = 360 - effectiveAngle
        requiredRotations = 360// effectiveRotation

        for i in range(requiredRotations):
            circle(length,360)
            right(angle)
            self.drawCircleCeption(angle-6, length)
        #end for loop
        
    #end circleCeption

#Uncomment for test run
#circ = circleCeption()
#circ.drawCircleCeption(139,90)

class triangleFractal:
    
    def getMid(self, p1,p2):
        #   (x_1 + x_2)    (y_1 + y_2) 
        #   -----------  , -----------  
        #        2              2
        return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2) #find midpoint

    def drawTriangle(self, size, depth):
        #create 3 points of the outter triangle
        a = size //2
        h = int(size * (math.sqrt(5) /4 ) )
        self.points = [ [-a , -h ] ,[0 , h],[a,-h]] 
        #call the funtion
        self.triangle(self.points ,depth)
    
    def triangle(self, points ,depth):
        up()
        goto(points[0][0],points[0][1])
        down()
        goto(points[1][0],points[1][1])
        goto(points[2][0],points[2][1])
        goto(points[0][0],points[0][1])

        if depth>0:
            self.triangle( [points[0],
                            self.getMid(points[0], points[1]),
                            self.getMid(points[0], points[2])],
                       depth-1)
            self.triangle([points[1],
                            self.getMid(points[0], points[1]),
                            self.getMid(points[1], points[2])],
                       depth-1)
            self.triangle([points[2],
                            self.getMid(points[2], points[1]),
                            self.getMid(points[0], points[2])],
                       depth-1)


#tf = triangleFractal()
#tf.drawTriangle(300 ,5)

class polySpiral:

    def drawPolySpiral(self, angle, length):

        self.angle = angle
        self.length = length
        
        
        for i in range (angle):
            forward(i*10)
            left(length)
        #end loop

#Uncomment for test run
#poly = polySpiral()
#poly.drawPolySpiral(50, 100)

class jaggedEdge:

    def drawJaggedEdge(self, angle, length):

        self.angle = angle
        self.length = length
        
        
        for i in range (angle):
            forward(i*2)
            right(length/2)
            back(angle)
            forward(angle/2)
            left(length)
            
        #end loop

#Uncomment for test run
#jagged = jaggedEdge()
#jagged.drawJaggedEdge(45, 50)

#end all 



