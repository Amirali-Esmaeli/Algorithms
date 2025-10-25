number = int(input())
world = []
for _ in range(number):
    world.append(input())
for i in range(number):
    if len(world[i]) > 10:
        print(world[i][0] + str(len(world[i])-2) + world[i][-1])
    else:
        print(world[i])