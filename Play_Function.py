import numpy as np
# creates a new function that allows category selection and point values into a box
# also allows for one error in spelling and can 

categories = ["exoplanets", "blackholes", "galaxies", "stars", "solar system"]
point_values = ["100", "200", "300", "400", "500"]

def play():
    category = int(input("Enter your catagory: exoplanets, blackholes, galaxies, stars, solar system"))

    if category not in categories:
        category = int(input("Please select a valid category: exoplanets, blackholes, galaxies, stars, solar system"))

    if category in categories:
        point_values = int(input("select point value: 100, 200, 300, 400, 500"))

        if point_values not in point_values:
            point_values = int(input("Please select a valid point value: 100, 200, 300, 400, 500"))

    return point_values, category

play()


    


