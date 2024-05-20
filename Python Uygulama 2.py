import math
points = [(5, 12), (3, 4), (0,0)]

def euclidean_distance(point1, point2):
    distance = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    return distance
distance_list =  []
for i in points:
    #print(i)
    for j in points:
        #print(j)
        if i == j:
            pass
        else:
            distance = euclidean_distance(i, j)
            print(distance)
            distance_list.append(distance)

print(min(distance_list))