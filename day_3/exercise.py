# age = input("What is your current age? ")
# height = input("What is your height in cm? ")
# complex_var = input("What is your favourite complex number? ")
# base = input("Enter base:")
# height = input("Enter height:")

# print("The area of the triangle is: " + str(0.5 * int(base) * int(height)) + "cm^2)")
# side_a = input("Enter side a:")
# side_b = input("Enter side b:")
# side_c = input("Enter side c:")
# print(
#     "The perimeter of the triangle is: "
#     + str(int(side_a) + int(side_b) + int(side_c))
#     + "cm)"
# )
# # Calculate the slope, x-intercept and y-intercept of y = 2x -2

# print("The slope is: " + str(2))
# # Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

# print("The slope is: " + str((10 - 2) / (6 - 2)))
# # Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# delta = 6**2 - 4 * 1 * 9
# # calculate the value of x
# x1 = (-6 + delta**0.5) / 2
# x2 = (-6 - delta**0.5) / 2
# print("Value y going to be 0")
# print("The value of x is: " + str(x1))
# print("The value of x is: " + str(x2))

# print(len("python") > len("jargon"))
# print("on" in "python" and "on" in "jargon")
# print("jargon" in "I hope this course is not full of jargon")
# length = float(len("python"))
# print(length)
# print(int("9.8") == 10)

# 23 Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3)
