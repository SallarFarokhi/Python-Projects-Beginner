import json
import random


with open("words_dictionary.json") as dictionary:
    words = json.load(dictionary)


dict = list(words.keys())


phrase = []
phrase2 = []
guessCount = 0

#userPhrase = input("What phrase do you want to guess for?")
#userLetter = input("What letter will you guess next?")


userPhrase = random.choice(dict)
for i in range(len(userPhrase)):
    phrase.append(userPhrase[i].lower())


phrase2 = phrase.copy()
for i in range(len(phrase)):
    if phrase2[i] != " ":
        phrase2[i] = "_"


def complete():
    for i in range(len(phrase2)):
        if phrase2[i] == "_":
            return True

    return False


print("Welcome to the hangman game!")


while complete():
    userLetter = input("\nWhat letter will you guess now? ")
    try:
        foo = phrase.index(userLetter)
    except:
        guessCount += 1
    for i in range(len(phrase)):
        if userLetter == phrase[i]:
            phrase2[i] = userLetter
    if len(userLetter) > 1:
        print("You stupid bitch, why are you guessing more than one letter?")
    if len(userLetter) == 0:
        print("You stupid bitch, why didn't you guess a letter?")
    if guessCount == 10:
        print("\nYou have run out of guesses, you stupid bitch")
        print("\nThe word was " + phrase)
        break
    for i in range(len(phrase)):
        print(phrase2[i], end = " ")


if not complete():
    print("\nCongratulations, you have guessed the phrase!")




