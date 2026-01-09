import random

def scrambler():
    wordPool = ["pennsylvania"," representitive","peculiar","detartrated"]
    selectedword=''
    
    wordIndex = random.randrange(0,3)
if    wordIndex == 0:
    selectedword = wordPool = [1]
elif wordIndex == 1:
    selectedword = wordPool = [2]
elif wordIndex == 2:
    selectedword = wordPool = [3]
elif wordIndex == 3:

    if randomwordSelect == 0:
         correctWord = wordPool[0]
    elif randomwordSelect == 1:
         correctWord = wordPool[1]
    elif randomwordSelect == 2:
         correctWord[2]
    elif randomWordSelect == 3:
         correctword = wordPool[3]

    convertedWord = list(selectedword)
    random.shuffle(convertedWord)
    scrambledWord = "".join(convertedWord)

print("guess the correct word: "+ scrambled)
userGuess = input()

while attempt < 3:


    if userGuess == correctWord:
        print("congrats! that is correct")
        ateempt +=3
else:
     print("sorry,that is incorrect.")


scrambleWordGame()