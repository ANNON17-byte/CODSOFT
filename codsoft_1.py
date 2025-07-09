import random
class Pass:
  def __init__(self):
    self.le = int(input("Enter the length of the password: "))
    self.com = input("Enter the complexity of the password: easy/medium/hard ")
  def display(self):
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = "1234567890"
    d = "!@#$%^&*()_+"
    if self.com == "easy":
      print("Your password is","".join(random.choices(a, k = self.le)))
    elif self.com == "medium":
      print("Your password is","".join(random.choices(a+b, k =self.le)))
    elif self.com == "hard":
      print("Your password is","".join(random.choices(a+b+c+d, k = self.le)))
x = Pass()
x.display()
