import numpy as np
# creates a new function that allows category selection and point values into a box
# creates a loop that runs and go through all the catagories and point values
# if player miss spells a catagory or types one in that does not exist it will ask them select a vaild catagory
# the same will occur for the point value, but once a vaild combination of catagory and point value is selected the code will run 
# Had a problem with the .ipyn file able to run so we had to make it a .py so it would agree and work in the main run code.
# Actually also had a problem with the indentation for an if statement, but was able to fix it by just removing the extra indent so now the player is able to make an error when typing point values and the code will still run.

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




    


