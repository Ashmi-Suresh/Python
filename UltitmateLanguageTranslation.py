'''
Program: Ultimate Language Translation
Author: Ashmi Bidrupane Suresh
Purpose: Program to translate words from one language to another
Revisions: 
    00: To print announcement
    01: To open file and read data
    02: To create a list of tuple to contain data 
    03: To create a 'while True' loop to continuously get words from users
    04: To create conditions to look up and return the respective word
    04: To create conditions to add new words to the lists
    05: To create break to exit the loop
    06: To write new words to the file
    
'''

# To open the vocabulary file and read its content
with open('vocabulary.txt') as f:
    # Create a list of tuples to contain the vocabulary data
    data = [(tuple(line.split())) for line in f.readlines() if line.strip()]
    
# To print an announcement to the user
print("Program to translate words from English to French and vice-versa")   

# To create an infinite loop that prompts the user to enter a word
while True:
    # To convert the user input to lowercase
    word = input("\nEnter an English or French word to translate: ").lower()
    
     # To check if the word is in the English vocabulary
    if word in [pair[0] for pair in data]:  
        # If the word is in the English vocabulary, print its French equivalent
        print(f"The English word '{word}' is '{data[[pair[0] for pair in data].index(word)][1]}' in French")
        
        # To check if the word is in the French vocabulary
    elif word in [pair[1] for pair in data]:   
        # If the word is in the French vocabulary, print its English equivalent
        print(f"The French word '{word}' is '{data[[pair[1] for pair in data].index(word)][0]}' in English")
        
        # If the user input is empty, break out of the loop
    elif word == '':   
        print('Exiting ...')
        break

     # If the word is not in either vocabulary, prompt the user to add it
    else:  
        print(f"The word '{word}' was not found in English or French dictionaries!")
        if input(f"Would you like to add '{word}' to the dictionaries? <y>es or <n>o ").lower() in ['y','yes']:
            lang_Option = input(f"What language is '{word}' in? <E>nglish or <F>rench ").lower()
            
             # If the user specifies that the word is in English
            if lang_Option in ['e','eng','english']:  
                # Prompt the user for the French equivalent and add the new word pair to the vocabulary
                data.append(tuple([(word),input(f"What is the French word for '{word}'? ").lower()]))
                print('The new words have been added the dictionaries.')

             # If the user specifies that the word is in French   
            elif lang_Option in ['f','fre','french']:
                
                # Prompt the user for the English equivalent and add the new word pair to the vocabulary
                data.append(tuple([input(f"What is the English word for '{word}'? ").lower(),(word)]))
                print('The new words have been added the dictionaries.')
                
                 # If the user input is invalid, prompt them to try again
            else:  
                print(f"The language '{lang_Option.capitalize()}' was not found. Please try again!")

            # Write the new vocabulary data to the file    
            with open('vocabulary.txt','w') as f:   
                for line in data:
                    f.write(f'{line[0]} {line[1]}\n')
            # If the user chooses not to add the word, prompt them to try again        
        else:
            print('Let\'s try again!')   
