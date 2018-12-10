
import random
import math
import matplotlib.pyplot as plt

# ----------------------------------------- Extra Credit ----------------------------------------------------
# ------------------------------------------ Will Brown -----------------------------------------------------

# Approximating Pi using the Monte Carlo Method 

# Edit this value to change the number of randomly generated points

points = [1000, 10000, 100000, 1000000]

results = {}
percent = {} 

# Generate random a set of random X and y Coordinates that fall within the rectangle
def makeCoords(): 
    x = random.random()
    y = random.random()
    return x,y

total_points = 0 
in_circle = 0

# Split the phone number in half use the upper digit values for the x value 
# and the lower digits for the y value. Divide by 100,000 to put all values between 0 and 1

def plotPoint():
    global total_points
    global in_circle

    x,y = makeCoords()
    total_points += 1 

    # calculate the euclidean distance between this point and the origin, if it is less 
    # than or equal to one, we are within the circle
    if (math.sqrt(x*x + y*y) <= 1):
            in_circle += 1


# Approximate PI based on 4 * (points in)/(total points) 

def calcPI(number_in, total):
    return 4 * number_in/total

# create and plot the number of points

for number_of_points in points: 
    for x in range(number_of_points):
        plotPoint()
        pi_approx = calcPI(in_circle, total_points)
        results[number_of_points] = pi_approx

def percentError(value):
        return abs((pi_approx - math.pi)/math.pi * 100)
# -------------------------- Run Program -------------------------------

print("Approximate Value: ")    
print(pi_approx)
print("Percent Error: ")
print(percentError(pi_approx))
keys = list(results.keys())
values = list(results.values())
plt.plot(keys,values)
plt.show()
input("Press Enter to End.")

