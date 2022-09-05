
import random
import Hangman_words_list #or from Hangman_words_list import word_list, then can omit Hangman_words_list.
import Hangman_art # or from Hangman_art import logo, stages
import os #for clear 

print(Hangman_art.logo)
chosen_word = random.choice(Hangman_words_list.word_list)
#Testing code
word_length = len(chosen_word)
# print(f'Pssst, the solution is {chosen_word}.')
#create blanks
display = []
for _ in range(word_length): #range the no of words, so to repeat _ printing
  display+="_"
print (f"{' '.join(display)}")
#Guess a letter
lives = 6
end_of_game = False
while not end_of_game:
  guess = input("Guess a letter: ").lower()
#check guess letter, then a loop to continue while game not end yet 
  os.system('cls') #clear command for terminal from os
  if guess in display:
    print(f"You've already guessed {guess}")

  for position in range(word_length):
    letter =chosen_word[position]
    if letter == guess:
      display[position] = letter
  if guess not in chosen_word:
    lives -= 1
    print (f"You guessed {guess}, that's not in the word. You lose a life.\n")
    print (Hangman_art.stages[lives])
    if lives == 0:
        end_of_game = True
        print(f"You Lose!, the word is {chosen_word}")
  
  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("End of game, you win!")

  




