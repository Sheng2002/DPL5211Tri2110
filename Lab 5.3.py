#  Student ID: 1201200814
#  Student Name: Tan Zhi Sheng

def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter

def meter_to_cm(meter):
    centimeter = meter / 100
    return centimeter

def get_cm():
    cm=float(input("Please enter a value for centimeter :"))
    m = cm_to_meter(cm)
    print(" {} cm is {} meter ".format(cm,m))

def get_meter():
    m=float(input("Please enter a value for meter :"))
    cm = meter_to_cm(m)
    print(" {} meter is {} cm ".format(m,cm))

option=int(input("Select function 1 or 2:"))

if(option==1):
    get_cm();

elif(option==2):
    get_meter();

else :
    print("Invalid choise")



