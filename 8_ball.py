import random
name = input("Enter your name: ")
question = "What the future holds for you?"
answer = ''
random_number = random.randint(1,9)
#Prints random number from 1 to 9
print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Ask again later."
elif random_number == 5:
  answer = "It is decidedly so."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My souces say no."
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

print(name + " asks: " + question)
print("Magic 8_Ball's answer: " + answer)
