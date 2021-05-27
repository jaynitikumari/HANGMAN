#done and dusted
import string
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''

    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the worpld correctly )
      return False (wrong selection)
    '''
    
    guessed_word=get_guessed_word(secret_word,letters_guessed)
    if secret_word==guessed_word:
    	return True
    return False

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    total_letters='abcdefghijklmnopqrstuvwxyz'
    string=''
    for i in total_letters:
    	if i in letters_guessed:
    		string=string+'_'
    	else:
    		string=string+i
    letters_left = string
    return letters_left

def isValid(letter):
	
	if len(letter)==1 and ord(letter)>=97 and ord(letter)<=122:
		return True
		
	return False
	
def hint(secret_word,letters_guessed):
	guessed_word=get_guessed_word(secret_word,letters_guessed)
	for i in range(len(secret_word)):
		if secret_word[i]!=guessed_word[i]:
			print(secret_word[i])
			break
	
def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format( str(len(secret_word))), end='\n\n')
    
    print()
    print("Enter HINT for hint.")    

    letters_guessed = []
    hint_val=1
    count=0
    while count<8:

   	 available_letters = get_available_letters(letters_guessed)
   	 print("Available letters: {} ".format(available_letters))
   	 guess=input("Please enter a letter:")
   	 letter=guess.lower()
   	 
   	 if hint_val>0:
 	   	if letter=="hint":
 	   		hint(secret_word,letters_guessed)
 	   		hint_val-=1
 	   		continue
   	 
   	 if not isValid(letter):
 	   	print("Invalid Entry.")
 	   	continue
   	 
   	 if letter in secret_word :
   	 	print("Right Choice!!")
   	 	letters_guessed.append(letter)
   	 	print("Good guess: {} ".format( get_guessed_word(secret_word, letters_guessed)))
   	 	print("Remaining Lives:","* "*(8-count))
   	 	if is_word_guessed(secret_word, letters_guessed) == True:
     		   
        	    print(" * * Congratulations, you won! * * ", end='\n\n')
        	    break
   	 else: 
 	       print("Wrong Choice!")
 	       print("Oops! That letter is not in my word: {} ".format( get_guessed_word(secret_word, letters_guessed)))
 	       letters_guessed.append(letter)
 	       print(IMAGES[count])
 	       count+=1
 	       print("Remaining Lives:","* "*(8-count))
 	       if count==8:
    	    	print("Oh-Ooh....You Lose!\n Better Luck Next Time.")
    	    	print("The secret word is :",secret_word)
 	      	 
 	       
    	    
	

# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
