import random

map_name = input("Enter a name for the map: ")
x = int(input("How long X: "))
y = int(input("How long Y: "))

##Constants
low = 0
high = 5

row,col = (x,y)

# map_array = [[0]*x]*y
map_array = [[0] * x for _ in range(y)]

map_array[0][0] = 1

def randomize_matrix(matrix,low,high):
    map_array = matrix
    for i in range(len(map_array)):
        for element in range(len(map_array[i])):
            map_array[i][element] = random.randint(low,high)
    return matrix

map_array = randomize_matrix(map_array,low,high)

for row in map_array:
    final_map = print(" ".join(map(str,row)))


with(open(f'{map_name}.txt', "w")) as file:
    for row in map_array:
        file.write(" ".join(map(str,row)) + "\n")