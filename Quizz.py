print('welcome To the game')

playing=input('Do you want to play? ').lower()

if playing != 'yes':
    quit()

print('lets play')
score=0


answer= input('what does GPU stand for? ').lower()

if answer=='graphical processing unit':
    print('Correct')
    score+=1
else:
    print('Incorrect')

answer= input('what does PSU stand for? ').lower()

if answer=='power switch unit':
    print('Correct')
    score+=1
else:
    print('Incorrect')

answer= input('what does RAM stand for? ').lower()

if answer=='random access memory':
    print('Correct')
    score+=1
else:
    print('Incorrect')

print(f'You have {score} number of question.')
print(f'You have {(score)/4*100} number of question.')