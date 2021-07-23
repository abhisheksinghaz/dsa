# question link: https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

class print_dupes:
  def __init__(self):
    
    # accepting the input from the user
    self.s = input("Enter a string: ")

  def output(self):
    
    # 'set(self.s)' will have all the characters of the entered string just once.
    for ele in set(self.s):
      if self.s.count(ele) > 1:
        print("count of " + ele + " = " + str(self.s.count(ele)))

if __name__ == "__main__":
  obj = print_dupes()
  obj.output()
