'''
import math


def find_least_distance(coord1, coord2, coord3):
    """
    Calculates the distances between three coordinates and prints the coordinates with the least distance.
    
    Parameters:
    coord1, coord2, coord3: tuples of length 2 containing the x and y coordinates of a point
    
    Returns:
    None
    """
    distances = []
    distances.append(
        math.sqrt((coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2))
    distances.append(
        math.sqrt((coord3[0]-coord1[0])**2 + (coord3[1]-coord1[1])**2))
    distances.append(
        math.sqrt((coord3[0]-coord2[0])**2 + (coord3[1]-coord2[1])**2))

    min_distance = min(distances)

    if min_distance == distances[0]:
        print(
            f"The coordinates {coord1} and {coord2} have the least distance of {min_distance:.2f}.")
    elif min_distance == distances[1]:
        print(
            f"The coordinates {coord1} and {coord3} have the least distance of {min_distance:.2f}.")
    else:
        print(
            f"The coordinates {coord2} and {coord3} have the least distance of {min_distance:.2f}.")

find_least_distance((1,1),(5,4),(10,2))
'''

'''
import math

def distance(x1, y1, x2, y2, x3, y3):
    d1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    d2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    d3 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    
    distances = {'(x1, y1) and (x2, y2)': d1,
                 '(x2, y2) and (x3, y3)': d2,
                 '(x1, y1) and (x3, y3)': d3}
    
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    
    print(f"The distances are: {sorted_distances[0][0]} - {sorted_distances[0][1]}")
    
    return sorted_distances[0][1]

distance(1,1,5,4,6,3)
'''

import math
def distance_between_coordinates(coord1, coord2, coord3):
    """
    Finds the distance between 3 coordinates using the Pythagorean theorem.
    Returns the set of coordinates with the least distance.
    """
    # Calculate the distances between all pairs of coordinates
    dist_12 = math.sqrt((coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2)
    dist_13 = math.sqrt((coord3[0]-coord1[0])**2 + (coord3[1]-coord1[1])**2)
    dist_23 = math.sqrt((coord3[0]-coord2[0])**2 + (coord3[1]-coord2[1])**2)

    # Determine which pair of coordinates has the least distance
    if dist_12 <= dist_13 and dist_12 <= dist_23:
        return coord1, coord2
    elif dist_13 <= dist_12 and dist_13 <= dist_23:
        return coord1, coord3
    else:
        return coord2, coord3


# Example usage:
coord1 = (0, 0)
coord2 = (3, 4)
coord3 = (5, 6)
closest_coords = distance_between_coordinates(coord1, coord2, coord3)
print("The closest coordinates are:", closest_coords)
