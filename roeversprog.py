# [[file:README.org::*Udvikling af logik][Udvikling af logik:1]]
# Dette er et modul til oversættelse mellem almindelige sprog og røversprog
import re

consonanter = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Z"]

def oversaet_til_roeversprog(inputtekst):

    outputtekst = [i + "o" + i if i in consonanter else i for i in inputtekst]
    # we use list comprehension to simplify our translation and avoid making a long if else loop.
    outputtekst = "".join(outputtekst) # we use the .join() method to join the list into a string.
    print(outputtekst)
    return outputtekst


def oversaet_fra_roeversprog_til_andet_sprog(inputtekst):
 #although i tried to use list comprenhention here, it didn't work as expected
 # as we need to replace a pattern of character several places
 # instead of replacing each character on the str like in our other function, therefore we use a for loop
    for i in consonanter: # loop through each consonant
        inputtekst = re.sub((i+"o"+i), i, inputtekst) # replace the pattern with the consonant
    outputtekst = [i for i in inputtekst] # we create a new list from the input
    outputtekst = "".join(outputtekst) # we use the .join() method to join the list into a string.
    print(outputtekst)
    return outputtekst

# Udvikling af logik:1 ends here
