class Calc:
  def __init__(self):
    self.n1 = int(input("Enter the first number:"))
    self.n2 = int(input("Enter the second number:"))
  def display(self):
    op = input("Specify the operation to be performed : +,-,*,/ = ")
    if op == '+':
      print("The result is",self.n1 + self.n2)
    elif op == '-':
      print("The result is",self.n1 - self.n2)
    elif op == '*':
      print("The result is",self.n1 * self.n2)
    elif op == '/':
      print("The result is",self.n1 / self.n2)
x = Calc()
x.display()
