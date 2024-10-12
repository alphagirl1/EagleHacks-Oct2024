# This is used to send clear screen for each letter
import os
# This is used to generate a random number from 1 to 1296, to get a random word
from random import randrange

#Set up the first word before the loop
#Initialize score and hearts
score=0
hearts=8
wordsdone=0
guesses=[] #store current guesses so we dont double count them
message="Welcome to Vocardio. Good luck!" #Message to the user after each try
# Open the file with the word list
file=open("wlist.txt", "r")
content=file.readlines()
#pick a random number from 0 to 1295
wordnum=randrange(1295)
#Each word takes 4 lines - word, info1, info2, sentence
#Remove the last char each line because thats the newline character
currword=content[wordnum*4][:-1]
currword=currword.upper()
info1=content[wordnum*4+1][:-1]
info1=info1.upper()
info2=content[wordnum*4+2][:-1]
info2=info2.upper()
sentence=content[wordnum*4+3][:-1]
sentence=sentence.upper()
#Hide the word in the sentence with asterixes
sentence=sentence.replace(currword,"*"*len(currword))
currentguess="-"*len(currword)
file.close()
while True:
    os.system('cls')
    print("============== V O C A R D I O ==============\n\n"+message+"\n")
    print("FIND THE WORD:     "+currentguess+" ("+str(len(currword))+")")
    print("\n")
    print(info1+"\n"+info2+"\n"+sentence+"\n")
    for i in range(hearts):
        print("\u2764\ufe0f", end="  ")
    print("\n")
    print("Words Completed: "+str(wordsdone)+"     Score: "+str(score))
    print("\n")
    guess=input('Type a single charcter and press enter, or type QUIT to quit: ')
    guess=guess.upper()
    if guess=="": continue
    if guess=="QUIT":
        message="You quit the game"
        break    
    guess=guess[0] #Taking the first charcter in case multiple where entered
    if guess in guesses:
        message="You already guessed "+guess
        continue
    else:
        guesses.append(guess)            
    if guess in currword:
        newguess=""
        #This loop replaces the guess word with the correct guess letter in the correct position from currword, leaving the rest as is
        for i in range(len(currword)):
            if currword[i]==guess: 
                newguess+=guess
            else:
                newguess+=currentguess[i]
        currentguess=newguess
        if currentguess==currword:
            message="Yes! The word was "+currword
            if hearts==8:
                score+=100
            else:
                score+=hearts*10
            hearts=8
            wordsdone+=1
            guesses=[]
            file=open("wlist.txt", "r")
            content=file.readlines()
            #pick a random number from 0 to 1295
            wordnum=randrange(1295)
            #Each word takes 4 lines - word, info1, info2, sentence
            #Remove the last char each line because thats the newline character
            currword=content[wordnum*4][:-1]
            currword=currword.upper()
            info1=content[wordnum*4+1][:-1]
            info1=info1.upper()
            info2=content[wordnum*4+2][:-1]
            info2=info2.upper()
            sentence=content[wordnum*4+3][:-1]
            sentence=sentence.upper()
            #Hide the word in the sentence with asterixes
            sentence=sentence.replace(currword,"*"*len(currword))
            currentguess="-"*len(currword)
            file.close()
        else:
            message="Yes, it contains "+guess
    else:
        message="No, it does not contain "+guess
        hearts-=1
        if hearts==0:
            message="You ran out of hearts! GAME OVER"
            break
os.system('cls')
print("============== V O C A R D I O ==============\n\n"+message+"\n")
print("Words Completed: "+str(wordsdone)+"     Score: "+str(score))
print("\nThank you for playing Vocardio!")