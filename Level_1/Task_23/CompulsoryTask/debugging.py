def print_values_of(dictionary, *args): # Added *args to take more arguments
    for key in dictionary.keys(): # Add dictionary.keys() to get the keys
        if key in args: # Added if statement to check that the key is passed to print the value
            print(dictionary[key]) # Needs the word key because key is used in for loop

simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", "maggie": "(Pacifier Suck)"} # Needs double quotes / removed space before pacifier suck

print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

