import  pygame
from  math import  sqrt


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distant(self,b):
         self.dist = sqrt((b.x-self.x)**2+(b.y-self.y)**2)
         return(self.dist)
    def halfway(self,b) :
        self.h_x=(b.x+self.x)/2
        self.h_y=(b.y+self.y)/2
        return (self.h_x,self.h_y)

    def reflect(self):
        self.reflect_x= (self.x,-self.y)
        self.reflect_y= (-self.x,self.y)
        self.reflect_origin= (-self.x,-self.y)
        return (self.reflect_x,self.reflect_y,self.reflect_origin)

    def get_line_to(self,b):

        # phương trình đường thẳng qua 2 điểm
        # (y2-y1)(x-x1) +(-x2+x1)(y-y1)=0 khi a2+b2 !=0
        self.p=b.y-self.y
        # hệ số của x
        self.q=-b.x+self.x
        # hệ số của y
        self.l=(b.x-self.x)*self.y-(b.y-self.y)*self.x
        # hệ số tự do
        if self.p**2 +self.q**2 !=0:
            return(self.p,self.q,self.l)
# trả về hệ số của phương trình đường thẳng
    def distance(self,a,b):
        # tinh khoang cách từ 1 điểm bất kì đến các đường thẳng của hcn
        self.m, self.n, self.p = a.get_line_to ( b )
        self.d = abs ( self.m * self.x + self.n * self.y + self.p ) / ((self.m ** 2 + self.n ** 2) ** (1 / 2))
        return self.d

class Rectangle():
    def __init__(self,a,b,c):
        self.width = a.distant(b)
        self.height=a.distant(c)
        print("width ={0},height={1}".format(self.width,self.height))
    def area(self):
        self.s =self.width*self.height
        return(self.s)
    def primater(self):
        self.cv=(self.width+self.height)*2
        return (self.cv)

    def flip(self):
        [self.width, self.height] = [self.height, self.width]
        print("sau khi dao chieu dai va rong: ")
        print("Width = {0},Height = {1}".format(self.width, self.height))

    def find_d(self,a,b,c):
       self.d_x = b.x + c.x - a.x
       self.d_y = b.y + c.y - a.y
       return (self.d_x,self.d_y)
    def compare(self,a,b,c,d,e):
        if ((e.distance(a, b) + e.distance(c ,d )) == a.distant( c ) and (e.distance( a, c ) + e.distance( b, d )) == a.distant( b )):
            return True
        else:
            return False



a= Point(2,1)
b= Point(10,9)
c= Point(6,-3)
h_x,h_y = a.halfway(b)
dist  = a.distant(b)
reflect_x,reflect_y,reflect_origin=a.reflect()
p,q,l=a.get_line_to(b)
print("phuong trinh duong thang la: {0}x+({1})y+({2})=0".format(p,q,l))
print("trung diem cua  diem a ,b co toa do:x={0} , y={1} ".format(h_x, h_y))
print("khoang cach giua 2 diem la={0}".format(dist))
print("reflect_x={0},redlect_y={1},reflect_origin={2}".format(reflect_x,reflect_y,reflect_origin))



result = Rectangle(a,b,c)
s=result.area()
print("dien tich hinh chu nhat la: ",s)

cv=result.primater()
print("chu vi hinh chu nhat la: ",cv)

result.flip()

d_x, d_y = result.find_d ( a, b, c )
d=Point(d_x,d_y)
print("toa do diem d la x={0},y={1}".format(d_x,d_y))

e=Point(5,4)

if result.compare(a,b,c,d,e):
        print("E=({0},{1}) in ABCD".format(e.x,e.y))
else:
        print("E=({0},{1}) not in ABCD ".format(e.x,e.y))
