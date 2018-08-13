#Making a game of hangman
import random

def rand_word(file_name):
    # Retrieves a random word from a file
    
    with open(file_name) as f:
        words = f.readlines()
        
    answer = random.choice(words).strip()
    
    while len(answer) <= 4:
        answer = random.choice(words).strip()
        
    users_word = list("_" * len(answer))
    display_word(users_word)
    
    return users_word, answer

def guess(users_word, answer):
    #Gets users' guess and updates it
    
    remaining_guesses = 10
    game_over = False
    letters_guessed = []
    
    while remaining_guesses > 0 and game_over == False and users_word != answer:
        guess_correct = False
        users_guess = input("Enter a character or a word: ")
        
        if len(users_guess) == 1:
            
            if users_guess in letters_guessed:
                print("You've already tried that character!")
                remaining_guesses -= 1
                print ("Guesses left: " + str(remaining_guesses))
            else:
                letters_guessed.append(users_guess)
                for index, i in enumerate(answer):
                    if i == users_guess:
                        users_word[index] = i
                        guess_correct = True
                        
                if guess_correct == False:
                    remaining_guesses -= 1
                    
                if users_guess == answer or "".join(users_word) == answer:
                    print ("Congratualtions! You have guessed my word!")
                    users_word = list(answer)
                    game_over = True
                    
                else:
                    print ("Guesses left: " + str(remaining_guesses))

        elif len(users_guess) == len(answer):
            
            if users_guess == answer:
                print("Congratualtions! You have guessed my word!")
                users_word = list(answer)
                game_over = True
                
            else:
                print("Unlucky try again!")
                remaining_guesses -= 1
        else:
            print("Incorrect input! That's going to cost you a guess!")
            remaining_guesses -= 1
            print ("Guesses left: " + str(remaining_guesses))

        display_word(users_word)
        
    if remaining_guesses == 0:
        print("Game Over!")
        print ("My word was " + answer)

    game_over = True
    
def display_word(users_word):
    #Displays the word the user is trying to guess
    
    print(" ".join(users_word))
    
replay = True
while replay:
    users_word, answer = rand_word("words.txt")
    guess(users_word, answer)
    wants_replay = input("Would you like to play again? Y or N? ")
    upper_replay = wants_replay.upper()
    
    while upper_replay != "Y" and upper_replay != "N":
        wants_replay = input("Would you like to play again? Y or N? ")
        upper_replay = wants_replay.upper()
    
    if upper_replay == "Y":
        pass
    elif upper_replay == "N":
        replay = False
    

                
    
