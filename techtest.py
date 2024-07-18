import numpy as np

directions = {'East': [1, 0], 'West': [-1, 0], 'North': [0, 1], 'South': [0, -1]}

points = {
    1: {'x': 28, 'y': 42, 'dir': 'North'},
    2: {'x': 27, 'y': 46, 'dir': 'East'},
    3: {'x': 16, 'y': 22, 'dir': 'South'},
    4: {'x': 40, 'y': 50, 'dir': 'West'},
    5: {'x': 8, 'y': 6, 'dir': 'North'},
    6: {'x': 6, 'y': 19, 'dir': 'East'},
    7: {'x': 28, 'y': 5, 'dir': 'South'},
    8: {'x': 39, 'y': 36, 'dir': 'West'},
    9: {'x': 12, 'y': 34, 'dir': 'North'},
    10: {'x': 36, 'y': 20, 'dir': 'East'},
    11: {'x': 22, 'y': 47, 'dir': 'South'},
    12: {'x': 33, 'y': 19, 'dir': 'West'},
    13: {'x': 41, 'y': 18, 'dir': 'North'},
    14: {'x': 41, 'y': 34, 'dir': 'East'},
    15: {'x': 14, 'y': 29, 'dir': 'South'},
    16: {'x': 6, 'y': 49, 'dir': 'West'},
    17: {'x': 46, 'y': 50, 'dir': 'North'},
    18: {'x': 17, 'y': 40, 'dir': 'East'},
    19: {'x': 28, 'y': 26, 'dir': 'South'},
    20: {'x': 2, 'y': 12, 'dir': 'West'},
}

def get_dist(point1: list, point2:list) -> float:
    # function to return distance between two points
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]

    return (x**2+y**2)**(0.5)

def get_dot_product(vect1 : np.array, vect2: np.array) -> int:
    # return dot product of two vectors i.e x1*x2 + y1*y2...
    return np.dot(vect1, vect2)


def get_mod_of_vect(vect: np.array) -> float:
    # return modulous of a vectors i.e sqrt(x**2 + y**2)
    return np.linalg.norm(vect)

test_points = {
    1: {'x': 28, 'y': 42, 'dir': 'North'},
    2: {'x': 20, 'y': 38, 'dir': 'East'}
    }

def main(row: int, max_degrees: float, radius: float) -> list: 

    # declare return variable "valid points" plus define input point (anchor_point) paramters, i.e point to check x, y and convert into a vector.
    # direction vector is retrived from directions object at top of script.

    valid_points = []
    current_row = points[row]
    x, y = current_row['x'], current_row['y']
    anchor = [x, y]
    anchor_vect = np.array([x, y])
    direction_vector = np.array(directions[current_row['dir']])

    # Logic I use to see if point is visible:
    # Step 1: Check to see if distance between point A (anchor_point) and point B (point_to_check) is greater than radius. If so then the point cannot be visible so continue.
    # Step 2: Check to see if the angle bewteen Point A and Point B, relative to direction, is less than maximum_degrees. i.e If direction in 'North' and angle is 45 degrees, then only points 45 degree "either side" of the direction vector are valid
    # Step 3: If step 2 and 3 are vlid, append relevant results to valid_points

    for row_num in points.keys():

        if row_num == row:
            continue

        row_to_check = points[row_num]
        xx, yy = row_to_check['x'], row_to_check['y']

        dist = get_dist(anchor, [xx, yy])
        if dist > radius:
            continue

        point = [xx, yy]
        point_vect = np.array(point)

        direction_vect_to_point = point_vect - anchor_vect
        angle = np.arccos(
            get_dot_product(direction_vector, direction_vect_to_point) / 
            (get_mod_of_vect(direction_vector)*get_mod_of_vect(direction_vect_to_point))
        )

        angle_in_degrees = np.rad2deg(angle)

        if angle_in_degrees <= (max_degrees): 
            valid_points.append([row_to_check['x'], row_to_check['y'], row_num, row_to_check['dir']])

    return valid_points

row = input('Please enter row number: ')
degrees = input('Please enter degree of cone (i.e width): ')
radius = input('Please enter radius of cone: ')

print(main(int(row), float(degrees), float(radius)))
