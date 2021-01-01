import myfunctions

switch_case = {
    1: myfunctions.randomgen,
    2: myfunctions.rockpaperscissor,
    3: myfunctions.sinecosinecurve,
    4: myfunctions.passwordgen,
    5: myfunctions.hangman,
    6: myfunctions.binarysearchcall,
    7: exit
    }

while (1):

    print('Hello!! Select options \n 1. Guess the Number \n 2. Rock paper Scissors Game \n 3. Sine vs Cosine curve \n 4. Password generate'
      '\n 5. hangman game \n 6. Binary Search Algorithm \n 7. Exit')
    a = input("Select your option: ")
    switch_case[int(a)]()
    a=input("Play again(y/n)")
    if a == 'n': exit(1)
