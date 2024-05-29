import random
print("welcome to number guessting game")
print("im thinking of a number between 1 and 100")
maxiumguesses = 0
randomnumber= random.randint(1,100)
while maxiumguesses < 5:
  guess = int(input("what is your guess?"))
  if (guess== randomnumber):
    print('you win')
    break
  elif(guess < randomnumber):
    print('too low')
  elif(guess > randomnumber):
    print('too high')
  maxiumguesses += 1
  