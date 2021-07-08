import random

def MinMax(arr):
  print("Input list: "+str(arr))
  arr_len = len(arr)
  if 0 == arr_len: 
    return "The list is empty"
  elif 1 == arr_len:
    return (arr[0],arr[0])
  else:
    min = arr[0]
    max = arr[0]
    for index in range(1, len(arr) ):
      if arr[index] > max:
        max = arr[index]
      if arr[index] < min:
        min = arr[index]
    return (min, max)

if __name__ == "__main__":
  #creating a list with length from 5 to 10, consisting of integer values ranging from -100 to 100
  arr = [random.randint(-100,100) for i in range(random.randint(5,10))]
  print(MinMax(arr))
