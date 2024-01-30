
'''
Program: Language Translation
Author: Ashmi Bidrupane Suresh
Purpose: Program to translate words from one language to another
Revisions: 
    00: To print announcement
    01: To create a dictionary and add words of different languages
    02: To create a 'while True' loop to continuously get words from users 
    03: To create conditions to look up and return the respective word
    04: To create conditions to add new words to the lists
    05: To create break to exit the loop
'''
#To create a dictionary and add words of different languages
colors = {}   
colors['red'] = {}
colors['red'].update({'french':'rouge'})
colors['red'].update({'spanish':'rojo'})
colors['red'].update({'german':'rot'})
colors['green'] = {}
colors['green'].update({'french':'vert'})
colors['green'].update({'spanish':'verde'})
colors['green'].update({'german':'grun'})
colors['yellow'] = {}
colors['yellow'].update({'french':'jaune'})
colors['yellow'].update({'spanish':'amarillo'})
colors['yellow'].update({'german':'gelb'})
colors['blue'] = {}
colors['blue'].update({'french':'bleu'})
colors['blue'].update({'spanish':'azul'})
colors['blue'].update({'german':'blau'})

#To print announcement
print("Language Translator")   

#To create a 'while True' loop to continuously get words from users
while True:  
    print(f"\nAvailable English words are: {'; '.join([k for k in colors.keys()])}")
    word = input("Please enter a color in English: ").lower()
    #To create conditions to look up and return the respective word
    if word in colors.keys():  
        print('Available language translations are: german; french; spanish')
        if (language := input('Please enter a language from the list: ').lower()) in colors['red'].keys():
            print(f"The word '{word}' in {language.capitalize()} is '{colors[word][language]}'.")
        else:
            print(f"Language '{language.capitalize()}' was not found. Please try again!")
    elif word == '':
        #To create break to exit the loop
        print('Exiting ...')  
        break
    #To create conditions to add new words to the lists
    else:    
        if input(f"The English word '{word}' was not found. Would you like to add '{word}' to the dictionary? <y>es or <n>o ").lower() in ['y','yes']:
            colors[f"{word}"] = {}
            colors[f"{word}"].update({'french': (input(f"What is the French word for {word}? ")).lower()})
            colors[f"{word}"].update({'spanish': (input(f"What is the Spanish word for {word}? ")).lower()})
            colors[f"{word}"].update({'german': (input(f"What is the German word for {word}? ")).lower()})
            print('The new words have been added to the dictionary!')
        else:
            print('Let\'s try again!')
        
