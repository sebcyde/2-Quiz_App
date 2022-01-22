print('hello world')
playing = input('Do you want to play a game? Y/N ')
if playing != 'y':
    quit()

print("Okay, let's play!")
answer = input('What does CPU stand for? ')
if answer == 'central processing unit':
    print('Correct!')
else: print("Incorrect!")

print("Not bad. Let's try another one!")
answer2 = input('What is the best front end framework? ')
if answer2 == 'react':
    print('Right again!')
else: print("Incorrect!")

continueplaying = input("Okay, should we try some more? Y/N ")
if continueplaying != 'y':
    quit()

print("Alright, let's do some general knowledge instead.")
answer3 = input('In which country does the Louvre reside? ')
if answer3 == 'france':
    print('Nice!')
else: print("ahh too bad, that not correct")

answer4 = input('Next, who painted the Mona Lisa? ')
if answer4 == 'leonardo da vinci':
    print('okay, lets make them more difficult then...')
else: print("ahh too bad, that not correct")

answer5 = input('Another art one, who created the Ascension of Polka Dots, 2006? ')
if answer5 == 'yayoi kusama':
    print('I know you googled that... but okay, lets carry on!')
else: print("ahh too bad. Try using google next time lol")

# answer6 = input('Another art one, who created the Ascension of Polka Dots, 2006? ')
# if answer6 == 'yayoi kusama':
#     print('I know you googled that... but okay, lets carry on!')
# else: print("ahh too bad, that not correct. Try using google next time lol")