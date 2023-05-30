import random  #random Import
from xtermcolor import colorize  #color words in the output

print("Welcome to " + colorize("Hangman!", ansi=4))

wordArray = []  #wordsArray
hangWords = open("words.txt", "r")  #read the file from words.txt

for wordK in hangWords:  #for word in the file
    wordArray.append(wordK)  #wordArray append the word
#after that:
wordMan = random.choice(
    wordArray)  #the hangman word is chosen randomly from wordArray
wordMan = wordMan.strip()  #the hangman word is stripped from any whitespaces

print("Your word is a " +
      colorize(str(len(wordMan)) + "-letter word.", ansi=3))  #hangman word in yellow (looks orange)


def printOrigin():  #print ("_ _ _ _)
    for i in range(0, len(wordMan)):  #for in range of wordMan's length
        print("_", end=" ")


printOrigin()  #printOrigin(), show how many letters there are
print("")  #newline
print("")  #newline
print("Put down your guess of a letter.")

letT = ""  #the actual word to see if it is the hangmword or not
numGu = 0  #guesses done variable
solvedC = False  #solved or not variable
usedArray = []  #used words Array
foundArray = []  #founded words Array
trialW = {}  #trialObject to see if letT == the wordMan
actualG = int(
    len(wordMan) * 1.35 + 1
)  #guess are *1.35 the number of letters in the word you are supposed to guess (+1)
for j in range(0, len(wordMan)):  #for in range of wordMan's length
    trialW[j] = "_"  #since not solved yet, it will set to "_"

while letT != wordMan:  #while letT != wordMan
    print("")
    letterG = input("Put Down A Guess: ")  #input
    if numGu != actualG:  #checks if the number of guesses used is equal to the number of guesses allowed
        if len(letterG) == 1:  #only one letter, not more than one
            if letterG not in usedArray:  #checks if the user already tried the letter
                usedArray.append(
                    letterG
                )  #appends a used letter so the user knows it already tried the letter at the end
                correctC = False  #got a correct letter = false
                for letx in wordMan:  #for character in the hangman word
                    if letx == letterG:  #if character = the input
                        correctC = True  #makes it not go to the correctC == False statement
                        print(colorize("Correct!", ansi=22))
                        foundArray.append(
                            letterG
                        )  #foundArray appends it to know that the player found one letter
                if correctC == False:
                    print(colorize("Incorrect!", ansi=1), end=" ")
                    numGu += 1  #number of Guesses +1
                if actualG - numGu == 0:  #checks if the player has zero guesses or not, if so he or she __import__
                    break
                    #he or she lost, breaks while loop
                if actualG - numGu > 1 or actualG - numGu == 0:  #if guesses left > 1, print with 'guesses'
                    print("You have " +
                          colorize(str(actualG - numGu), ansi=3) +
                          " guesses left!")
                else:  #else print with 'guess' (same down into the false area)
                    print("You have " +
                          colorize(str(actualG - numGu), ansi=3) +
                          " guess left!")
                if len(foundArray) == 0:
                    printOrigin()  #"_ _ _ _"... (no letters found)
                else:
                    foundNum = 0  #counting variable ~ foundArray
                    appendingNum = 0  #counting variable ~ trialW Object
                    exceptStr = 0  #for except purposes, since you need something there
                    for k in range(
                            0, len(wordMan)
                    ):  #to check for each letter in wordMan of length
                        appendingNum = 0  #reset counting variable for trialW object
                        for charA in wordMan:  #for letter in the hangman word
                            try:  #sees if there is an index error
                                vals = foundArray[
                                    foundNum]  #validate foundArray[foundNum]
                            except IndexError:  #if there is an index error, skip :), just +=1 for exceptStr
                                exceptStr += 1  #for except purposes, since you need something there
                            else:  #if no error:
                                if trialW[
                                        appendingNum] == "_":  #if the object has "_", if it doesn't, just skip (which means it got found)
                                    if charA == foundArray[
                                            foundNum]:  #check if it matches the letter in wordMan
                                        trialW[
                                            appendingNum] = charA  #if so, it will become the charA (letter) instead when printed instead of "_"
                            appendingNum += 1  #counting variable += 1 so it can move on to the next "_" or character in the object
                        foundNum += 1  #next object in the foundArray
                    letT = ""  #letT = "" (reset)
                    for charB in trialW:  #for object in trialW
                        letT = letT + trialW[
                            charB]  #letT  = letT + the object[charB]
                        print(trialW[charB],
                              end=" ")  #print it, with no new line
                    if letT == wordMan:  #checks if the letT equals the actual hangman word
                        solvedC = True  #if so, solvedC = True
                        print("")  #newline
                        print(
                            colorize(letT, ansi=22) +
                            " was the word! You won! Run again to try another word."
                        )
                        break
                        #breaks, since it got solved
                print("Used Letters: " +
                      str(usedArray))  #used letters, prints the usedArray
            else:
                print("You have already used that letter! Try another one.")
        else:
            print("One letter please!!!"
                  )  #only one letter please with (len) up in the if statement
    else:
        break
        #breaks because there are no more guesses left

if solvedC == False:  #if False, print this since he or she lost, if not, just exit the program
    print("You failed! The word was " + colorize(wordMan, ansi=1) +
          ". Press the " + colorize("Run Button", ansi=22) +
          " to Try Again.")  #reveals word in red, and to run again in green
