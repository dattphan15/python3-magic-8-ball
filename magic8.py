import random

name = "Kevin"
question = "Is Python3 the latest Python version?"
answer = ""

# generate a random number between 1 (inclusive) and 9 (inclusive).
random_number = random.randint(1, 12)

# prints a random number
print("Random number: " + str(random_number))

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "You've guessed it right."
elif random_number == 11:
  answer = "Listen to your inner spirit."
else:
  answer =  "Error"
    

# prints name of the person who printed the question if it exists.
if name:
  print(name + " asks: " + question)
else:
  print("Question: " + question)

# prints answer
print("Magic 8-Ball's answer: " + answer)