import random
import numpy as np
import matplotlib.pyplot as plt
import re
import os


#Check is user number matches the random generated number
def randomgen():
    x = input("type your guess number between 1-10")
    #generates a random number between 0-9
    y = random.randrange(10)
    if x == y:
        print("You won")
    else:
        print("your number:", x, " does not match the random generated number", y)


#rock -> scissor -> paper -> rock game.
def rockpaperscissor():
    #create list variable
    v_rockpaperscissor=['rock','scissor','paper']
    x=input("type rock, scissor, paper")
    #get a random value between 0-2
    r=random.randrange(3)
    #use the random value to choose one from rockpaperscisser list
    y=v_rockpaperscissor[r]
    if (x=='rock' and y=='scissor') or (x=='scissor' and y=='paper') or (x=='paper' and y=='rock'):
        print(x+" win over "+y)
    elif ( x == y ):
        print(x+" draws "+y)
    else:
        print(x+" lose over "+y)

#plot sin cosine curve using matplotlib
def sinecosinecurve():
    #sine wave = amplitude of a cyclic variation by time given by A*sin(w*t), where w=frequency
    #below numpy used to get range of values from 0 to 4pi with interval of 0.1
    time = np.arange(0,4*np.pi,.1)
    amplitude1 = np.sin(time) #amplitude of sin curve at given time interval
    amplitude2 = np.cos(time) #amplitude of cos curve at given time interval
    plt.plot(time,amplitude1,time,amplitude2) #plot sin and cos
    plt.title('Sin vs Cos Wave from 0 to 4pi')
    plt.xlabel('Time 0 to 4pi')
    plt.ylabel('Amplitude = sin(time) and cos(time)')
    plt.grid(True, which='both')
    plt.legend(['sin(x)','cos(x)'])
    plt.axhline(y=0,color='k')
    plt.interactive(False)
    #plt.plot([1,2,3,4])
    plt.show(block=True)

#generate password
def passwordgen():
    #get all characters allowed for password
    s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#%$&*()?"

    #random.seed(2016)  #seed can be used to get same random password for retrieving.
    p="".join(random.sample(s,8))
    print("Your Password: "+p)


#hangman identify the name game
def hangman():
    #get main script directory path
    path=os.path.dirname(__file__)
    print("path:"+path)
    #read file having words for hangman game
    with open(path+"/resources/word.txt") as f:
        word_list = f.read().splitlines()
    f.close()
    #get a random word
    random_num = random.randint(0,len(word_list)-1)
    word_chosen=list(word_list[random_num])
    #encode word to hypen(-)
    encoded_word = list('-'*len(word_chosen))
    #    list(re.sub('[a-zA-Z]','-',word_list[random_num]))
    print("word:" + "".join(word_chosen))
    print("word"+"".join(encoded_word))
    #start the game with 5 lives
    HANGMANPICS = ['''
    +---+
        |
        |
        |
        |
    =======''',
    '''
    +---+
    O   |
        |
        |
        |
    =======''','''
    +---+
    O   |
    |   |
        |
        |
    =======''',
    '''
     +--+
     O  |
    /|  |
        |
        |
    =======''',
    '''
     +--+
     O  |
    /|\ |
        |
        |
    =======''',
    '''
     +--+
     O  |
    /|\ |
     |  |
        |
    =======''',
    '''
     +--+
     O  |
    /|\ |
     |  |
    /   |
    =======''',
    '''
     +--+
     O  |
    /|\ |
     |  |
    / \ |
    ======='''
    ]
    i=0
    while(i<len(HANGMANPICS)):
        letter=input("Enter your guess letter:")
        if letter not in word_chosen:
            i = i + 1
            if i >= len(HANGMANPICS):
                print(HANGMANPICS[len(i)])
                print("You Lose")
            else:
                print(HANGMANPICS[i])
                print("Wrong Guess. You have ", len(HANGMANPICS)-i, " more guesses left")
        else:
            #check if guess letter exists in guess word
            for x in range(len(word_chosen)):
                if word_chosen[x]==letter:
                    encoded_word[x] = word_chosen[x]

        decode_word="".join(encoded_word)
        print(HANGMANPICS[i])
        print(decode_word)

        if decode_word==word_list[random_num]:
            print("You Won")
            break

#binary search recursive function to find an int value from array
def binarysearch(arr,left, right, val):
    #check difference of provided search indexes are greater than 0 or not
    #if diff > 0 then, get mid value
    if right >= left:
        mid = int(left + (right - left)/2)
        #check mid value matches, greater, less than the user provided value
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            #if mid value greater than user value, call binary search again with left of mid indexes
            return binarysearch(arr,left,mid-1,val)
        else:
            # if mid value less than user value, call binary search again with right of mid indexes
            return binarysearch(arr,mid+1,right,val)
    else:
        return -1
#function to call binary search
def binarysearchcall():
    r=random.randint(1,3)
    print("r",r)
    x=0
    numlist = []
    for i in range(1,100,r):
        #numlist.extend([None]*(x-len(numlist)+1))
        numlist.append(i)
        x = x + 1
    print(numlist)
    p=input("your number to binary search")
    result=binarysearch(numlist,0,len(numlist)-1,int(p))
    if result != -1:
        print("Element present at index:", result)
    else:
        print("Element is not present in array")
