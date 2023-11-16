import math
 
class MyShape:
    def __int__(self, side, length, width, radius):
        side
        length
        
        radius
    def square(side):
        return side*side
 
    def rectangle(length,width):
        return length*width
 
    def round(radius):
        pi = math.pi
        return radius*radius*pi
 
S = int(input("输入正方形邊長："))
print("正方形面積 : ", MyShape.square(S))
 
L = int(input("输入長方形的長："))
W = int(input("输入長方形的寬："))
print("長方形面積 : ", MyShape.rectangle(L,W))
 
R = int(input("输入圓形半徑："))
print("圓形面積", MyShape.round(R))