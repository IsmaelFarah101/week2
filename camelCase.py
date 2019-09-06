import string
def camelCase(sentence):
    #fetches user input and using capwords to capitlize the first letter of each word and lower case the rest
    newsentence = string.capwords(sentence).replace(" ","")
    ## this lowercases the first letter of the word
    newsentence = newsentence[0].lower() + newsentence[1:]

    print(newsentence)

def instructions():
    message = 'Here are some instructions'
    stars = '*' * 20
    instruction = 'Enter a a wild sentence into the input'
    print(f'\n{stars}\n{message}\n{stars}')

def banner():
    message = 'Camel Case Generator'
    slashes = '/' * 20
    print(f'\n {slashes}\n{message}\n{slashes}')

def main():
    banner()
    instructions()
    userInput = input('Enter a clunk sentence: ')
    print(camelCase(userInput))

if __name__ == '__main__':
    main()