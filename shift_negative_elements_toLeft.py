import copy

arr = [1,2,3,5,9,7,6,-18,-3,-6,-77,8,50,-90,-65,44,-44]
# making a copy to verify with the original list in the end, as such not needed for carrying out this operation
arr2 = copy.deepcopy(arr)

ptr = 0
# for loop for iterating through all the elements of the list
for index in range(len(arr)):
  # finding the negative entries
  if arr[index] < 0 :
    # putting the negative element to the leftmost index i.e., starting from 0
    arr.insert(ptr, arr[index])
    # post this step the index value of the current element will increase by 1 and the list will have two entries of this element in particular

    # as the index value of this element has increased by 1, because of the insert command in the previous step
    # i am using the pop function on "index + 1" and not "index"
    arr.pop(index+1)

    # increasing the pointer value to enable the insertion of the next negative element at the next index and not overwrite the current element.
    ptr += 1
print(arr)

# Un-comment the following to verify that no element has been lost during the operation.
#print(len(arr) - len(arr2))
#print(set(arr2) - set(arr))
