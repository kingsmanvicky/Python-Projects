#HANGMAN GAME WITH PYTHON
import random
import hw 
import logo

#Creating the list of the ASCII of the figures of Hangman 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo.l)


choosen_word = random.choice(hw.word_list)
lives =6

 #Generating the same amount of dashes based on the choosen word
display =[]
for i in range(len(choosen_word)):
    display += '_'
print(display)

#Creating while loop to run the process again and again untill the word is fully guessed
end_of_game = False
while(end_of_game == False):


    #Getting the input and converting them to lowercase
    guess = input("Guess a letter: ").lower()


    #Swapping the dash with guessed letter if the letter in the choose_word
    for position in range(len(choosen_word)):
        if choosen_word[position] == guess:
            display[position] = guess
    print(display)

    if guess not in choosen_word:
        lives -=1
        if lives == 0:
            end_of_game = True
            print("YOU LOOSE!!")

    if "_" not in display:
        end_of_game = True
        print("YOU WON!!")
    print(stages[lives])





