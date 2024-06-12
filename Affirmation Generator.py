import random

print("😃The Affirmation Generator😃")
def affirmation_generator():
  affirmations = random.randint(1,5)
  if affirmations == 1:
    print("You are amazing!")
  elif affirmations == 2:
    print("You are loved!")
  elif affirmations == 3:
    print("You are epic!")
  elif affirmations == 4:
    print("You are cool!")
  elif affirmations == 5:
    print("You are impressive!")

affirmation_generator()
affirmation_generator()
affirmation_generator()
affirmation_generator()
affirmation_generator()

