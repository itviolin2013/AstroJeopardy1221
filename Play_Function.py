import numpy as np
from AI_Setup import prompt_llm


categories = ["exoplanets", "blackholes", "galaxies", "stars", "solar system"]
point_values = ["100", "200", "300", "400", "500"]

def play():
    category = input("Enter your catagory: exoplanets, blackholes, galaxies, stars, solar system")

    if category not in categories:
        category = input("Please select a valid category: exoplanets, blackholes, galaxies, stars, solar system")

    if category in categories:
        point_value = input("select point value: 100, 200, 300, 400, 500")

        if point_value not in point_values:
            point_value = input("Please select a valid point value: 100, 200, 300, 400, 500")
   
    return point_value, category
    



    


