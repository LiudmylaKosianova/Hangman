# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    for char in secret_word:
        if char  not in letters_guessed:
            return False
    return True
        


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    blueString = ''
    for char in secret_word:
        if char in letters_guessed:
            blueString = blueString + char
        else:
            blueString = blueString + '_ '
    return blueString



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    whiteString = string.ascii_lowercase
    blueString = ''
    for char in whiteString:
        if char not in letters_guessed:
            blueString = blueString + char
    return blueString


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    my_word_2 = ''
    for char in my_word:
       if char != ' ':
          my_word_2 = my_word_2 + char    


    if len(my_word_2) != len(other_word):
        
       return False
    
    for i in range (len(my_word_2)):
       if (my_word_2[i] != '_') and (my_word_2[i] != other_word[i]):
           
          return False
    
    list1 = []
    for char in my_word_2:
       if char != '_':
          list1.append(char)
    
    list2 = []
    for char in other_word:
       if char in list1:
          list2.append(char)
    
    letter_count1 = {}
    for char in list1:
        if char in letter_count1:
          letter_count1[char] += 1
        else:
          letter_count1[char] = 1
    
    letter_count2 = {}
    for char in list2:
        if char in letter_count2:
          letter_count2[char] += 1
        else:
          letter_count2[char] = 1
    
    if letter_count1 != letter_count2:
       return False
           
    return True

 


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass

    
    matches_list = []

    for word in wordlist:
       if match_with_gaps(my_word, word):        
          matches_list.append(word)
    if len(matches_list) == 0:
       print('No matches found')
    else:
       print('Possible word matches are:')
       print(" ".join(matches_list))



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    guesses = 6
    warnings = 3
    letters_guessed = []
    vowels = ['a', 'e', 'o', 'i', 'u']
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ', len(secret_word), ' letters long.')    

    can_play = True

    while can_play:
        
      print('-------------')
      print('You have ', guesses, ' guesses left.')
      print('Available letters: ', get_available_letters(letters_guessed))
      letter = input('Please guess a letter: ')

      if letter == '*':
         show_possible_matches(get_guessed_word(secret_word, letters_guessed))
         continue

      if not letter.isalpha():
        #check the warnings
        print('Oops! That is not a valid letter.')
        if warnings > 0:
          warnings -= 1
          print('You have ', warnings, ' warnings left: ', get_guessed_word(secret_word, letters_guessed))
          continue
        else:
          guesses -= 1
          print('You have no warnings left, so you lose one guess: ', get_guessed_word(secret_word, letters_guessed))
          continue
        
      letter.lower()

      if letter in letters_guessed:
        print('Oops! You have already guessed that letter.')
        #check the warnings
        if warnings > 0:
          warnings -= 1
          print('You have ', warnings, ' warnings left: ', get_guessed_word(secret_word, letters_guessed))
          continue
        else:
          guesses -= 1
          print('You have no warnings left, so you lose one guess: ', get_guessed_word(secret_word, letters_guessed))
          continue
                
      letters_guessed.append(letter)
            
      if letter in secret_word:
        print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed):
          print('----------')
          print('Congratulations, you won!')
          break
      else:
        print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
        if letter in vowels:
          guesses-=2
        else:
          guesses -=1
        
      if guesses <= 0:
        can_play = False
        print('----------')
        print('Sorry, you ran out of guesses. The word was ', secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #pass

  
    # To test hangman_with_hints comment out the pass line and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
