#Set sentence variable
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog"

#printing original sentence with replacement
print(sentence.replace("!", " "))

#Added another variable to avoid code duplication
sentence_moded = sentence.replace("!"," ").upper()

#Printing sentence with all letters in caps
print(sentence_moded)

#Printing capped sentence in reverse
print(sentence_moded[::-1])