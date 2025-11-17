#to import something from another file we can use "from file_name import function_name"
from local_and_global_declaration import area_of_a_circle
radius = float(input("Enter the value of radius: "))
area= area_of_a_circle(radius)
#print("The area of the circle is:{:.2f}".format(area))
print("The area of the circle is: %.2f"%area)