import string
sentence = input('Enter a clunk sentence: ')
#fetches user input and using capwords to capitlize the first letter of each word and lower case the rest
newsentence = string.capwords(sentence).replace(" ","")
## this lowercases the first letter of the word
newsentence = newsentence[0].lower() + newsentence[1:]

print(newsentence)

