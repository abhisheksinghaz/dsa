# question link: https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

s = input("Enter a string: ")

for ele in set(s):
  if s.count(ele) > 1:
    print("count of " + ele + " = " + str(s.count(ele)) )
