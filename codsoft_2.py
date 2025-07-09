
import random
class Game:
  def __init__(self):
    print("Choose rock/paper/scissor")
    self.choice = input()
  def display(self):
    print("------------------------")
    ch = random.choice(["rock","paper","scissor"])
    if self.choice == ch:
      print("You chose",self.choice)
      print("Computer chose",ch)
      print("It's a draw")
    elif self.choice == "rock" and ch == "paper":
      print("You chose",self.choice)
      print("Computer chose",ch)
      print("You lost")
    elif self.choice == "rock" and ch == "scissor":
      print("You chose",self.choice)
      print("Computer chose",ch)
      print("You won")
    elif self.choice == "paper" and ch == "rock":
      print("You chose",self.choice)
      print("Computer chose",ch)
      print("You won")
    elif self.choice == "paper" and ch == "scissor":
      print("You chose",self.choice)
      print("Computer chose",ch)
      print("You lost")
    elif self.choice == "scissor" and ch == "paper":
      print("You chose",self.choice)
      print("Computer chose",ch)
      print("You win")
    elif self.choice == "scissor" and ch == "rock":
      print("You chose",self.choice)
      print("Computer chose",ch)
      print("You lost")
  def again(self):
    print("------------------------")
    print("Type Yes if you want to play again and No if you want to quit")
    self.choice = input()
    if self.choice == "Yes":
      print("------------------------")
      y = Game()
      y.display()
      y.again()
    else :
      print("Thanks for playing")
      print("------------------------")
x = Game()
x.display()
x.again()
