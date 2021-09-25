import random

name = "Kevin"
question = "Is Python3 the latest Python version?"
answer = ""

# generate a random number between 1 (inclusive) and 9 (inclusive).
random_number = random.randint(1, 9)

# prints a random number
print(random_number)

if random_number == 1:
  answer = "Yes - definitely."

# prints answer
print(answer)