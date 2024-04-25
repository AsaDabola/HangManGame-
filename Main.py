# By Asa Daboh

import random
body_parts = ["o","/","|\\", "/", "\\"]
counter = 3

def print_hangman(counter, guessed_letter): 
  temp_body = body_parts[:counter]+[" "] * (len(body_parts)-counter)
  hangman = [
   " |------|",
   " |      {}".format(temp_body[0]),
   " |     {}{}".format(temp_body[1], temp_body[2]),
   " |     {} {}".format(temp_body[3], temp_body[4]),
   " |",
   " |",
   "_|_",
  ]

  print(*hangman, sep="\n")

def random_line(afile):
  line = next(afile)
  for num, aline in enumerate(afile, 2):
    if random.randrange(num):
      continue
    line = aline
  return line 


file = open("words.txt")

random_word = random_line(file)

if random_word[-1] == '\n':
  random_word = random_word[:-1]

guess = ['_']*len(random_word)

guessed_letters = set()
guessed_len = 0

def clear_screen():
  print('\n'*500)
  print_hangman(counter, guessed_letters)
  print(*guess, end="\n")

while counter < len(body_parts) and guessed_len < len(random_word):
  clear_screen()
  next_guess = input("Guess another letter: ").lower()
 
  while (next_guess in guessed_letters):
    print(f"You've already guessed {next_guess}")
    next_guess = input("Guess another letter: ").lower()

  correct_indeces = [i for i, letter in enumerate(random_word) if letter == next_guess]

  for i in correct_indeces:
    guess[i] = next_guess
    guessed_len +=1


  if len(correct_indeces) < 1: 
    counter +=1

  guessed_letters.add(next_guess)

clear_screen()

if counter == 5:
  print(f"You lose :( \nThe correct word was {random_word}")
else:
  print("You Won :)")
