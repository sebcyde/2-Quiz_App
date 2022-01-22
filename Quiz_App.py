print('hello world')
playing = input('Do you want to play a game? Y/N ')
if playing != 'y':
    quit()

print("Okay, let's play!")
answer = input('What does CPU stand for? ')
if answer == 'central processing unit':
    print('Correct!')
else: print("Incorrect!")

print("Let's try another one!")
answer2 = input('What is the best front end framework? ')
if answer2 == 'react':
    print('Correct!')
else: print("Incorrect!")

continueplaying = input("Should we try another one? Y/N ")
if continueplaying != 'y':
    quit()

print("Okay, let's carry on!")
answer3 = input(' ')
if answer3 == '':
    print('Correct!')
else: print("Incorrect!")


print("Let's try another one!")
answer2 = input(' ')
if answer2 == '':
    print('Correct!')
else: print("Incorrect!")