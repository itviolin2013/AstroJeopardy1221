import numpy as np
# creates a new function that allows category selection and point values into a box
# also allows for one error in spelling and can 

categories = ["exoplanets", "galaxies", "constellations", "solar system", "moons", "astronomers"]
point_values = ["100", "200", "300", "400", "500"]

def play():
    category = input("Enter your catagory: exoplanets, galaxies, constellations, solar system, moons, astronomers")

    if category not in categories:
        category = input("Please select a valid category: exoplanets, galaxies, constellations, solar system, moons, astronomers")

    if category in categories:
        point_values = input("select point value: 100, 200, 300, 400, 500")

        if point_values not in point_values:
            point_values = input("Please select a valid point value: 100, 200, 300, 400, 500")

    return point_values, category

play()


    


