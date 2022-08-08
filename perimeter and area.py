import math


class Calculate:
    s=0
    def perimeter(self,s1=None,s2=None,s3=None):
        if s1!=None and s2!=None and s3!=None:
            s=s1 + s2 + s3
        elif s1!=None and s2!=None:
            s=2 * (s1 + s2)
        else:
            s=2 * math.pi * s1
        return s

    a=0
    def area(self,s1=None,s2=None,s3=None):
        if s1 != None and s2 != None and s3 != None:
            a =  ((1 / 2) * s1 * s1 * (math.sqrt(3) / 2))
        elif s1 != None and s2 != None:
            a =s1 * s2
        else:
            a = math.pi * s1 * s1
        return a

s1 = int(input("enter side:"))
s2 = int(input("enter side:"))
s3 = int(input("enter side:"))
d = Calculate()

print("perimeter of side1 ="+str(d.perimeter(s1)))
print("perimeter of side1 and side2 and side3 ="+str(d.perimeter(s1, s2, s3)))
print("area of side 1 = "+str(d.area(s1)))
print("area of side 1 and 2 = "+str(d.area(s1, s2)))
print("area of side 1 and side 2 and side 3 = "+str(d.area(s1, s2, s3)))