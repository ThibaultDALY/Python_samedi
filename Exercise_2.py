

# Create a function called Median(numbers), that calculates exactly that. Given a list of numbers calculate
# the “middle” one. In case of a even amount of numbers, calculate the average of the two middle ones.

# def Median(numbers):
#     numbers = []
#     if int(numbers.index)%2 == 0 :
#         print(numbers[])


# Create a function hotel cost that calculates the cost in function of the number of days with a rate of 140.
# Create a function that takes a city as argument and calculates the plane cost. the cities and related costs
# are Paris, London, Brussels, New York and 180, 220 , 240 and 500 respectively. Create a function
# rental_car_cost(days) where the cost per day is 40 and a discount of 50 for +7day trips. Write a function
# to calculate the total trip cost given the city and days. What is the cost of 7 days New York?

cost_of_night = 140

def hotel_cost(number_of_day):
    return number_of_day * cost_of_night
print(hotel_cost(7))

def plane_cost(city):
    plane = "Nab"
    if city == "Paris":
        plane = 180
    elif city == "London":
        plane = 220
    elif city == "Brussels":
        plane = 240
    else :
        plane = 500
    if plane != "Nab":
        return plane
print(plane_cost("Brussels"))

def rental_car_cost(days):
    if (days < 8):
        return days*40
    else :
        return (days*40)- 50
print(rental_car_cost(8))

def total_trip_cost(days,city):
    return hotel_cost(days)+plane_cost(city)+rental_car_cost(days)
print(total_trip_cost(7,"New york"))

# DICTIONARIES #

Billy = {
    "name" : "Billy",
    "homework" : [90.0, 97.0, 75.0, 92.0],
    "quizzes" : [88.0, 40.0, 94.0],
    "tests" : [75.0,90.0]
}

Joyce = {
    "name" : "Joyce",
    "homework" : [100.0, 92.0, 98.0, 100.0],
    "quizzes" : [82.0, 83.0, 91.0],
    "tests" : [99.0,97.0]
}

# Print out all key values pairs

def printKey(dict):
    for key, value in dict.items() :
        x = print(key, value)
    return x
printKey(Joyce)

# average of the class

def average(class):


