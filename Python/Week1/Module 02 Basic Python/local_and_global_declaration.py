PI= 3.1416#this is a global declaration 

def area_of_a_circle(radius):
    ##pi=3.14 #this is a local declaration
    #to use and modify global varibale from a local scope we must define global inside local scope
    global PI
    area=PI*pow(radius,2)
    return area
if __name__=="__main__":
    radius = float(input("Enter the value of radius: "))
    area= area_of_a_circle(radius)
    print("The area of the circle is: %.2f"%area)