#Making a game of hangman
import random

def rand_word(file_name):
    # Retrieves a random word from a file
    f = open(file_name, "r")
    for num_lines, words in enumerate(f):
        pass
    num_lines += 1
    print(num_lines)
    rand_line = random.randint(1,num_lines)
    print (rand_line)
    file = f.readlines()
    print(file)
    f.close()
    
rand_word("words.txt")
            
                
    
