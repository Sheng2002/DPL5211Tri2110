#  Student ID: 1201200814
#  Student Name: Tan Zhi Sheng

def rectangle(w,l):
    area=w*l
    return area

def triangle(w,l):
    area=w*l/2
    return area

i = 0
while(i<2):
    width=float(input("Enter width: "))
    length=float(input("Enter length: "))

    rectanglearea=rectangle(width,length)
    trianglearea=triangle(width,length)

    print("Rectangle area : {:.2f}".format(rectanglearea))
    print("Triangle area  : {:.2f}".format(trianglearea))
    i+=1