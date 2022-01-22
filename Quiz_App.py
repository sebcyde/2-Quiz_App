playing = input('Do you want to play a game? Y/N ')
if playing != 'y':
    quit()

print("Okay, let's play!")
score = 0
answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")
    print("Your score is " + str(score) + "/6 questions correct")
    quit()

print("Not bad. Let's try another one!")
answer2 = input('What is the best front end framework? ')
if answer2.lower() == 'react':
    print('Right again!')
    score += 1
else: 
    print("Incorrect!")
    print("Your score is " + str(score) + "/6 questions correct")
    quit()

continueplaying = input("Okay, should we try some more? Y/N ")
if continueplaying != 'y':
    print("Your score is " + str(score) + "/6 questions correct")
    quit()

print("Alright, let's do some general knowledge instead.")
answer3 = input('In which country does the Louvre reside? ')
if answer3.lower() == 'france':
    print('Nice!')
    score += 1
else: 
    print("ahh too bad, that not correct")
    print("Your score is " + str(score) + "/6 questions correct")
    quit()

answer4 = input('Next, who painted the Mona Lisa? ')
if answer4.lower() == 'leonardo da vinci':
    print('okay, lets make them more difficult then...')
    score += 1
else: 
    print("ahh too bad, that not correct")
    print("Your score is " + str(score) + "/6 questions correct")
    quit()

answer5 = input('Another art one, who created the Ascension of Polka Dots, 2006? ')
if answer5.lower() == 'yayoi kusama':
    print('I know you googled that... but okay, lets carry on!')
    score += 1
else: 
    print("ahh too bad. Try using google next time lol")
    print("Your score is " + str(score) + "/6 questions correct")
    quit()

answer6 = input('Alright, last one. Naruto or Dragonball Z? ')
if answer6.lower() == 'naruto':
    print("Ah! I see you're a man of culture aswell. Nice.")
    score += 1
elif answer6.lower() == 'dragonball z':
    print("Ah! I see you're a man of culture aswell. Nice.")
    score += 1

print("Your score is " + str(score) + "/6 questions correct")
quit()
