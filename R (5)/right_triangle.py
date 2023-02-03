# Cameron Wysocki
# 9/28/22
# Evidence 1

from calendar import c
from stringprep import c9_set
from tkinter.tix import INTEGER


first_name = input("Please enter your first name. ")
# Using first_name to properly welcome and dismiss the user
print("Hello, " + first_name + ", and welcome to my program.")
print("This program is used to calculate the area of a right triangle (in feet).")

length = float (input("Please enter the length of your triangle's base (in feet). "))

height = float (input("Please enter the height of your triangle (in feet). "))

area = ((length*height)/2)
# Math portion
print("The area of your triangle is " + str (area) + "sqft.")
print("Thank you for using my area-of-a-triangle program, " + first_name + "; goodbye.")