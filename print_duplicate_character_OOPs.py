# question link: https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

class print_dupes:
  def __init__(self):
    self.s = input("Enter a string: ")

  def output(self):
    for ele in set(self.s):
      if self.s.count(ele) > 1:
        print("count of " + ele + " = " + str(self.s.count(ele)))

if __name__ == "__main__":
  obj = print_dupes()
  obj.output()
