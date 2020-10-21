def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for i in secretWord:
        if i in lettersGuessed:
            count +=1
    if count == len(secretWord):
        return True
    else:
        return False




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ""
    for i in secretWord:
        if i in lettersGuessed:
            word += i
        else:
            word += "_ "
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    poop = ''
    alphabet = string.ascii_lowercase
    for i in alphabet:
        if i not in lettersGuessed:
            poop += i
    return poop
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed=[]
    numguesses = 8
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("------------")
    
    while numguesses > 0:
        print("You have " + str(numguesses) + " guesses left.")
        print("Available letters: ", getAvailableLetters(lettersGuessed))
        x = input("Please guess a letter: ")
    

        if x in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord,lettersGuessed))
            print("------------")

        elif x in secretWord:
            lettersGuessed += x
            print("Good guess: " + getGuessedWord(secretWord,lettersGuessed))
            print("------------")
            
            if getGuessedWord(secretWord, lettersGuessed) == secretWord:
                print("Congratulations, you won!")
                break

        elif x not in secretWord:
            lettersGuessed += x
            numguesses -= 1
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord,lettersGuessed))
            print("------------")
            
    if getGuessedWord(secretWord, lettersGuessed) != secretWord:
                print("Sorry, you ran out of guesses. The word was " + str(secretWord))



