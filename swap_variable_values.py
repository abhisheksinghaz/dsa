import random

v1 = random.random() #random.randint(-1000,1000)
v2 = random.random() #random.randint(-1000,1000)
print("Initial values: v1 -> "+str(v1)+" & v2 -> "+str(v2))

v1 = v1 + v2
v2 = v1 - v2
v1 = v1 - v2
print("Presenting the swapped values: v1 -> " + str(v1) + " & v2 -> " + str(v2))
