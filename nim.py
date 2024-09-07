import random

print("**********************************")
print("*                                *")
print("*  Welcome to the game of NIM!!  *")
print("*                                *")
print("**********************************")

print("")
print("On your turn, you take either 1, 2 or 3 matches. The one who takes the last match loses.")

print("")
print("You go first!")
print("")

matches = random.randrange(20)+20
winner=False

print("There are "+str(matches)+" matches")
print("i "*matches)

while (True):
  print ("")
  usertaken=input("How many would you like to take (1-3)? ")

  if int(usertaken)>3 or int(usertaken)<1:
      print("Cheat!")
      exit()
  else:
      matches=matches-int(usertaken)
      print("")
      print("There are "+str(matches)+" matches left")
      print("i "*matches)

      if matches==1:
          print("Congratulations, you are the winner!")
          exit()

      print("")
      print("Computer's turn!")
      computertaken=(matches-1)%4

      if computertaken==0:
          computertaken=random.randrange(3)

      print ("Computer takes "+str(computertaken)+" matches")
      matches=matches-computertaken

      print("")
      print("There are "+str(matches)+" matches left")
      print("i "*matches)

      if matches==1:
          print ("")
          print("Hard luck, computer is the winner!")
          exit()
